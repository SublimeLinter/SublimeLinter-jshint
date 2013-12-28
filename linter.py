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

from SublimeLinter.lint import Linter


class JSHint(Linter):

    """Provides an interface to the jshint executable."""

    syntax = ('javascript', 'html')
    cmd = 'jshint --verbose * -'
    regex = (
        r'^(?:(?P<fail>ERROR: .+)|'
        r'.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?P<message>.+) \((?:(?P<error>E)|(?P<warning>W))\d+\))'
    )
    selectors = {
        'html': 'source.js.embedded.html'
    }
    config_file = ('--config', '.jshintrc')

    def split_match(self, match):
        """
        Return the components of the match.

        We override this to catch linter error messages and place them
        at the top of the file.

        """

        if match:
            fail = match.group('fail')

            if fail:
                # match, line, col, error, warning, message, near
                return match, 0, 0, True, False, fail, None

        return super().split_match(match)
