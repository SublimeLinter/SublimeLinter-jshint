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
    language = 'javascript'
    cmd = ('jshint', '--verbose', '-')
    regex = r'^.+?: line (?P<line>\d+), col (?P<col>\d+), (?P<error>.+) \((?P<type>[EW]\d+)\)$'


class EmbeddedJSHint(JSHint):
    language = 'html'
    selector = 'source.js.embedded.html'
