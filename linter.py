import re
from SublimeLinter.lint import NodeLinter


class JSHint(NodeLinter):
    npm_name = 'jshint'
    cmd = ['jshint', '--verbose', '${args}', '-']
    regex = (
        r'^(?:(?P<fail>ERROR: .+)|'
        r'.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?P<message>'
        # undefined warnings
        r'\'(?P<undef>.+)\'.+(?=.+W098)'
        # duplicate key
        r'|.+\'(?P<duplicate>.+)\'.+(?=.+W075)'
        # camel case
        r'|.+\'(?P<no_camel>.+)\'.+(?=.+W106)'
        # using later defined
        r'|(.+)?\'(?P<late_def>.+)\'.+(?=.+W003)'
        # double declaration
        r'|(.+)?\'(?P<double_declare>.+)\'.+(?=.+W004)'
        # unexpected use, typically use of non strict operators
        r'|.+\'(?P<actual>.+)\'\.(?=.+W116)'
        # unexpected use of ++ etc
        r'|.+\'(?P<unexpected>.+)\'\.(?=.+W016)'
        # match all messages
        r'|.+)'
        # capture error, warning and code
        r' \((?:(?P<error>E\d+)|(?P<warning>W\d+))\))'
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
        # restore word regex to default each iteration
        self.word_re = NodeLinter.word_re

        if match:
            fail = match.group('fail')

            if fail:
                # match, line, col, error, warning, message, near
                return match, 0, 0, True, False, fail, None

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
                # highlight variables used before defined
                if warning == 'W003':
                    near = match.group('late_def')
                    col -= len(match.group('late_def'))

                # highlight double declared variables
                elif warning == 'W004':
                    near = match.group('double_declare')
                    col -= len(match.group('double_declare'))

                # now jshint place the column in front,
                # and as such we need to change our word matching regex,
                # and keep the column info
                elif warning == 'W016':
                    self.word_re = re.compile(r'\+\+|--')

                # mark the duplicate key
                elif warning == 'W075' and match.group('duplicate'):
                    near = match.group('duplicate')
                    col = None

                # mark the undefined word
                elif warning == 'W098' and match.group('undef'):
                    near = match.group('undef')
                    col = None

                # mark the no camel case key, cannot use safer method of
                # subtracting the length of the match, as the original col info
                # from jshint is always column 0, using near instead
                elif warning == 'W106':
                    near = match.group('no_camel')
                    col = None

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
