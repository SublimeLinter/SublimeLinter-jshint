from SublimeLinter.lint import NodeLinter


class JSHint(NodeLinter):
    npm_name = 'jshint'
    cmd = ['jshint', '--verbose', '${args}', '-']
    regex = (
        r'^.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?P<message>'
        # unexpected use of ++ etc
        r'|.+\'(?P<unexpected>.+)\'\.(?=.+W016)'
        # duplicate key
        r'|.+\'(?P<duplicate>.+)\'.+(?=.+W075)'
        # camel case
        r'|.+\'(?P<no_camel>.+)\'.+(?=.+W106)'
        # unexpected use, typically use of non strict operators
        r'|.+\'(?P<actual>.+)\'\.(?=.+W116)'
        # match all messages
        r'|.+)'
        # capture error, warning and code
        r' \((?:(?P<error>E\d+)|(?P<warning>W\d+))\)'
    )
    defaults = {
        'selector': 'source.js - meta.attribute-with-value',
        # `filename` will determine the config finding algo of jshint. We
        # fake a name for unsaved files bc we sadly cannot just point to a
        # folder.
        '--filename:': '${file:${folder}/unsaved.js}'
    }

    def split_match(self, match):
        """
        Return the components of the match.

        We override this to catch linter error messages and return more presise
        info used for highlighting.

        """
        if match:
            # now safe to proceed, no error occured with jshint
            error = match.group('error')
            warning = match.group('warning')
            message = match.group('message')
            # force line numbers to be at least 0
            # if not they appear at end of file
            line = max(int(match.group('line')) - 1, 0)
            col = int(match.group('col')) - 1
            near = None

            # Note: jshint usually produces a `col` value, but sometimes the
            # col points to the last char of the offending code. When a col is
            # given, we can simply adjust the size of the error using near bc
            # SublimeLinter will just take the length of near in that case.
            # So when you see `col -= ...` we just shift the beginning of the
            # error to the left.

            if warning:
                # unexpected use of ++ etc.
                if warning == 'W016':
                    near = match.group('unexpected')

                # mark the duplicate key
                elif warning == 'W075' and match.group('duplicate'):
                    near = match.group('duplicate')
                    col -= len(match.group('duplicate'))

                # mark the no camel case key
                elif warning == 'W106':
                    near = match.group('no_camel')
                    col -= len(match.group('no_camel'))

                # if we have a operator == or != manually change the column,
                # this also handles the warning when curly brackets are required
                elif warning == 'W116':
                    # match the actual result
                    near = match.group('actual')

                    # if a comparison then also change the column
                    if near == '!=' or near == '==':
                        col -= len(near)

            return match, line, col, error, warning, message, near

        return None
