#
# jshint.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-jshint
# License: MIT
#

from SublimeLinter.lint import Linter


class JSHint(Linter):
    language = ('javascript', 'html')
    cmd = 'jshint --verbose -'
    regex = r'^.+?: line (?P<line>\d+), col (?P<col>\d+), (?P<message>.+) \((?:(?P<error>E)|(?P<warning>W))\d+\)$'
    selectors = {
        'html': 'source.js.embedded.html'
    }
