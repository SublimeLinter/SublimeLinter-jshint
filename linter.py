#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the JSHint plugin linter class."""

import re
from SublimeLinter.lint import Linter


class JSHint(Linter):

    """Provides an interface to the jshint executable."""

    syntax = ('javascript', 'html')
    cmd = 'jshint --verbose * -'
    regex = (
        r'^(?:(?P<fail>ERROR: .+)|'
        r'.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?P<message>'
        # undefined warnings
        r'\'(?P<undef>.+)\'.+(?=.+W098)'
        # duplicate key
        r'|.+\'(?P<duplicate>.+)\'.+(?=.+W075)'
        # non strict operators
        r'|.+\'(?P<actual>.+)\'\.(?=.+W116)'
        # unexpected use of ++ etc
        r'|.+\'(?P<unexpected>.+)\'\.(?=.+W016)'
        # match all messages
        r'|.+)'
        # capture error, warning and code
        r' \((?:(?P<error>E)|(?P<warning>W))(?P<code>\d+)\))'
    )
    selectors = {
        'html': 'source.js.embedded.html'
    }
    config_file = ('--config', '.jshintrc', '~')

    def split_match(self, match):
        """
        Return the components of the match.

        We override this to catch linter error messages and place them
        at the top of the file.

        """

        # restore word regex to default each iteration
        self.word_re = None

        if match:
            fail = match.group('fail')
            error = match.group('error')
            warning = match.group('warning')
            message = match.group('message')
            code = match.group('code')
            line = int(match.group('line')) - 1
            col = int(match.group('col')) - 1
            near = None

            if fail:
                # match, line, col, error, warning, message, near
                return match, 0, 0, True, False, fail, None
            # mark the undefined word
            elif code == '098':
                col -= len(match.group('undef'))
            # mark the duplicate key
            elif code == '075':
                col -= len(match.group('duplicate'))
            # if we have a operator == or != manually change the column,
            # near won't work here as we might have multiple ==/!= on a line
            elif code == '116':
                self.word_re = re.compile(match.group('actual'))
                col -= len(match.group('actual'))
            # now jshint place the column in front,
            # and as such we need to change our word matching regex,
            # and keep the column info
            elif code == '016':
                self.word_re = re.compile('\+\+|--')

            return match, line, col, error, warning, message, near

        return match, None, None, None, None, '', None
