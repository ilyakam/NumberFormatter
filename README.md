# NumberFormatter - A Sublime Text Plugin

This [Sublime Text](http://www.sublimetext.com/) plugin formats plain numbers by adding a thousands separator to them. It also unformats them in reverse. See the [Features](#features) section below for details.

## Installation

* **Package Control**
  1. [Install Package Control](https://packagecontrol.io/installation)
  1. [Bring up the Command Palette](https://sublime-text.readthedocs.io/en/stable/reference/command_palette.html#how-to-use-the-command-palette) and type "Package Control: Install Package"
  1. Type "NumberFormatter" and press <kbd>enter</kbd>
* **Directly**
  1. Locate the `Packages` folder in the [data directory](http://docs.sublimetext.info/en/sublime-text-3/basic_concepts.html#the-data-directory)
  1. Download the [latest version of NumberFormatter](https://github.com/ilyakam/NumberFormatter/releases/latest)
  1. Extract the archive into the `Packages` folder
* **Development**
  1. [Follow the instructions on the `CONTRIBUTING` guide](./CONTRIBUTING.md#getting-started)

## Usage

* Linux: <kbd>ctrl</kbd><kbd>shift</kbd><kbd>comma</kbd>
* macOS: <kbd>command</kbd><kbd>shift</kbd><kbd>comma</kbd>
* Windows: <kbd>ctrl</kbd><kbd>shift</kbd><kbd>comma</kbd>

## Features:

As long as the number is partially or fully selected, or while the cursor is on the number, this plugin will format or unformat it in the following way:

| Before      | After       |
| ----------- | ----------- |
| `12345`     | `12,345`    |
| `12,345`    | `12345`     |
| `12345.67`  | `12,345.67` |
| `12,345.67` | `12345.67`  |

This plugin supports multiple cursors and multiple selections. It can process both formatted and unformatted numbers in one go.

## Options

To change the settings, simply edit the `NumberFormatter.sublime-settings` file that's included with the plugin:

* `decimal_separator` - the character that separates between whole and decimal numbers
* `thousands_separator` - the character that groups numbers in the thousands, millions, billions, etc.
* `format_thousands` - whether or not to add a thousands separator to numbers between 1000 and 9999

## Warnings

* Numbers with preceding zeros are formatted anyway (`000123` » `000,123`)
* When the `thousands_separator` is set to an empty space (`" "`), the whole number must be selected in order to unformat it (`12 345` » `12345`)

## Changelog

See [CHANGELOG.md](./CHANGELOG.md)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

See [LICENSE.md](./LICENSE.md)

## Software Credits

The development of this software was made possible using the following components:

* [Expand Selection to Whitespace](https://github.com/bits/ExpandSelectionToWhitespace-SublimeText) by Paul Sarena
  Licensed under: MIT License
