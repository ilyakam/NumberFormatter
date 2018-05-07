# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Fixed:
- Ensure non-numeric strings are ignored without any errors

## [1.0.0] - 2018-04-29 
### Added:
- Ability to format numbers by adding thousands separator(s): `12345` » `12,345`
- Ability to format numbers by removing thousands separator(s): `12,345` » `12345`
- Ability to choose any character for the decimal and thousands separators
- Ability to skip formatting four-digit numbers between `1000` and `9999`
