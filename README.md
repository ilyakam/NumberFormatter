# NumberFormatter - A Sublime Text Plugin

This [Sublime Text](http://www.sublimetext.com/) plugin formats plain numbers by adding a thousands separator to them. It also unformats them in reverse. See the [Features](#features) section below for details.

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

* Preceding zeros are stripped out: `000123` » `123`
* Trailing decimal zeros are stripped out: `0.123000` » `0.123`
* A missing leading zero is added to all decimal numbers: `.123` » `0.123`
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
