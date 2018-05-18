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

            if warning:
                # unexpected use of ++ etc.
                if warning == 'W016':
                    near = match.group('unexpected')

                # mark the duplicate key
                elif warning == 'W075' and match.group('duplicate'):
                    near = match.group('duplicate')
                    col -= len(match.group('duplicate'))

                # mark the no camel case key, cannot use safer method of
                # subtracting the length of the match, as the original col info
                # from jshint is always column 0, using near instead
                elif warning == 'W106':
                    near = match.group('no_camel')
                    col -= len(match.group('no_camel'))

                # if we have a operator == or != manually change the column,
                # this also handles the warning when curly brackets are required
                # near won't work here as we might have multiple ==/!= on a line
                elif warning == 'W116':
                    actual = match.group('actual')
                    # match the actual result
                    near = match.group('actual')

                    # if a comparison then also change the column
                    if actual == '!=' or actual == '==':
                        col -= len(actual)

            return match, line, col, error, warning, message, near

        return match, None, None, None, None, '', None
