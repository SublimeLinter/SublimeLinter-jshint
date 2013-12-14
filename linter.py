#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-jshint
# License: MIT
#

"""This module exports the JSHint plugin linter class."""

from SublimeLinter.lint import Linter


class JSHint(Linter):

    """Provides an interface to the jshint executable."""

    syntax = ('javascript', 'html')
    cmd = 'jshint --verbose -'
    regex = r'^.+?: line (?P<line>\d+), col (?P<col>\d+), (?P<message>.+) \((?:(?P<error>E)|(?P<warning>W))\d+\)$'
    selectors = {
        'html': 'source.js.embedded.html'
    }
