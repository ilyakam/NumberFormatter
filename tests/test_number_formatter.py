import os
import runpy
import sys
import types
import unittest
from unittest.mock import patch


def load_command_class():
  sublime_plugin = types.ModuleType("sublime_plugin")
  sublime_plugin.TextCommand = object
  stubs = {
    "sublime": types.ModuleType("sublime"),
    "sublime_plugin": sublime_plugin,
  }
  module_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                             "number_formatter.py")

  with patch.dict(sys.modules, stubs):
    return runpy.run_path(module_path)["FormatNumberCommand"]


FormatNumberCommand = load_command_class()


class IsNumberTests(unittest.TestCase):
  def setUp(self):
    self.command = FormatNumberCommand()
    self.command.decimal_separator = "."
    self.command.thousands_separator = ","

  def test_default_separators_reject_underscore_integer(self):
    self.assertFalse(self.command.is_number("1_000"))

  def test_default_separators_reject_underscore_decimal(self):
    self.assertFalse(self.command.is_number("1_000.50"))

  def test_default_separators_reject_underscore_exponent(self):
    self.assertFalse(self.command.is_number("1e1_0"))

  def test_default_separators_reject_repeated_underscores(self):
    self.assertFalse(self.command.is_number("1__000"))

  def test_default_separators_accept_numbers(self):
    for value in ("0", "1234", "+1234", "-1234", "1234.50", ".5",
                  "1,234", "+1,234.50", "-1,234.50", "1e10"):
      self.assertTrue(self.command.is_number(value), value)

  def test_default_separators_reject_nonnumeric_text(self):
    for value in ("", "hello", "1.2.3", "1,word"):
      self.assertFalse(self.command.is_number(value), value)

  def test_underscore_thousands_separator_is_removed_before_validation(self):
    self.command.thousands_separator = "_"

    for value in ("1_000", "1_000.50", "1__000", "1e1_0"):
      self.assertTrue(self.command.is_number(value), value)

  def test_underscore_decimal_separator_is_normalized_before_validation(self):
    self.command.decimal_separator = "_"

    for value in ("1234_5", "-1234_5", "1,234_5"):
      self.assertTrue(self.command.is_number(value), value)


if __name__ == "__main__":
  unittest.main()
