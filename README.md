SublimeLinter-jshint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-jshint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-jshint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [jshint](http://www.jshint.com/docs/).
It will be used with files that have the "JavaScript" syntax, or within `<script>` tags in HTML files.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, ensure that `jshint` (2.5.0 or later) is installed on your system.
To install `jshint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `jshint` (or globally with `-g`):
   ```
   npm install jshint
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` or `.zprofile` and not `.zshrc`.(reason: [here](http://www.sublimelinter.com/en/latest/installation.html) and [here](https://github.com/SublimeLinter/SublimeLinter3/issues/128))

Please make sure that the path to `jshint` is available to SublimeLinter.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

You can configure `jshint` options in the way you would from the command line, with `.jshintrc` files. For more information, see the [jshint docs](http://www.jshint.com/docs/). You may provide a custom config file by setting the linter’s `"args"` setting to `["--config", "/path/to/file"]`. On Windows, be sure to double the backslashes in the path, for example `["--config", "C:\\Users\\Aparajita\\jshint.conf"]`.

### Using with tabs

If you use tabs as your indentation, make sure you set the option `indent: 1` in your .jshintrc file. If not the wrong sections of the code will be highlighted.
