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

import os
from SublimeLinter.lint import Linter, util


class JSHint(Linter):

    """Provides an interface to the jshint executable."""

    syntax = ('javascript', 'html')
    executable = 'jshint'
    regex = (
        r'^(?:(?P<fail>ERROR: .+)|'
        r'.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?P<message>.+) \((?:(?P<error>E)|(?P<warning>W))\d+\))'
    )
    selectors = {
        'html': 'source.js.embedded.html'
    }

    def cmd(self):
        """
        Return a string with the command line to execute.

        We define this method because we want to use the .jshintrc files,
        and we can't rely on jshint to find them, because we are using stdin.

        """

        command = [self.executable_path, '--verbose', '*']

        # Allow the user to specify a config file in args
        args = self.get_user_args()

        if '--config' not in args:
            jshintrc = util.find_file(os.path.dirname(self.filename), '.jshintrc')

            if jshintrc:
                command += ['--config', jshintrc]

        return command + ['-']

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
