SublimeLinter-jshint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-jshint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-jshint)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [jshint](http://www.jshint.com/docs/). It will be used with files that have the “JavaScript” syntax, or within `<script>` tags in HTML files.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `jshint` is installed on your system. To install `jshint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `jshint` by typing the following in a terminal:
   ```
   npm install -g jshint
   ```
Or install `jshint` locally in your project folder (**you must have package.json file there**):
    ```
    npm init -f
    npm install jshint
    ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

**Note:** This plugin requires `jshint` 2.5.0 or later. Please note that the _indent_ option no longer reports warnings for bad indentation. https://github.com/jshint/jshint/releases/tag/2.5.0

### Linter configuration
In order for `jshint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `jshint` is installed and configured, you can proceed to install the SublimeLinter-jshint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `jshint`. Among the entries you should see `SublimeLinter-jshint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

You can configure `jshint` options in the way you would from the command line, with `.jshintrc` files. For more information, see the [jshint docs](http://www.jshint.com/docs/). The linter plugin does this by searching for a `.jshintrc` file itself, just as `jshint` does from the command line. You may provide a custom config file by setting the linter’s `"args"` setting to `["--config", "/path/to/file"]`. On Windows, be sure to double the backslashes in the path, for example `["--config", "C:\\Users\\Aparajita\\jshint.conf"]`.

The path to the `.jshintrc` file is cached, meaning if you create a new `.jshintrc` that should have precedence over the previous one (meaning it is closer to the .js file) you need to clear the cache for the linter to use the new `.jshintrc` You can clear the cache by going to: Tools > SublimeLinter > Clear Caches.

### Using with tabs

If you use tabs as your indentation, make sure you set the option `indent: 1` in your .jshintrc file. If not the wrong sections of the code will be highlighted.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
