# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added:
- Installation instructions to the `README`
- Command to "Format Numbers" to the Command Palette

### Fixed:
- Ensure that the repository name is addressed in the `CONTRIBUTING` guide

## [1.0.3] - 2018-05-14
### Fixed:
- Ensure that updating the settings take immediate effect

## [1.0.2] - 2018-05-13
### Fixed:
- Ensure that large numbers do not change due to rounding when formatted
- Ensure that empty selected regions do not throw an error in the console
- Ensure that a useless decimal dot (e.g., `1234.`) doesn't count as a digit

## [1.0.1] - 2018-05-06
### Fixed:
- Ensure non-numeric strings are ignored without any errors

## [1.0.0] - 2018-04-29 
### Added:
- Ability to format numbers by adding thousands separator(s): `12345` » `12,345`
- Ability to format numbers by removing thousands separator(s): `12,345` » `12345`
- Ability to choose any character for the decimal and thousands separators
- Ability to skip formatting four-digit numbers between `1000` and `9999`
