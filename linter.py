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
    regex = r'^.+?: line (?P<line>\d+), col (?P<col>\d+), (?P<message>.+) \((?:(?P<error>E)|(?P<warning>W))\d+\)$'
    selectors = {
        'html': 'source.js.embedded.html'
    }

    def cmd(self):
        """
        Return a string with the command line to execute.

        We define this method because we want to use the .jshintrc files,
        and we can't rely on jshint to find them, because we are using stdin.

        """

        command = ['jshint', '--verbose']
        jshintrc = util.find_file(os.path.dirname(self.filename), '.jshintrc')

        if jshintrc:
            command += ['--config', jshintrc]

        return command + ['*', '-']
