SublimeLinter-jshint
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [jshint](http://www.jshint.com/docs/). It will be used with files that have the “JavaScript” syntax, or within `<script>` tags in HTML files.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Installation).

### Linter installation
Before installing this plugin, you must ensure that `jshint` is installed on your system. To install `jshint`, do the following:

1. Install [Node.js](http://nodejs.org).

1. Install `jshint` by typing the following in a terminal:
   ```
   npm install -g jshint
   ```

Once jshint is installed, you can proceed to install the SublimeLinter-jshint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `jshint`. Among the entries you should see `SublimeLinter-jshint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Settings). For information on generic linter settings, please see [Linter Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Linter-Settings).

You can configure `jshint` options in the way you would from the command line, with `.jshintrc` files. For more information, see the [jshint docs](http://www.jshint.com/docs/).

**Note:** The linter plugin does this by searching for a `.jshintrc` file itself and setting the `--config` option if it finds one, so you cannot use that option in the linter’s `"args"` setting.

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
