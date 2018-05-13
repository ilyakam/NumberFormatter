import re
import sublime
import sublime_plugin

settings = sublime.load_settings("NumberFormatter.sublime-settings")

decimal_separator = settings.get("decimal_separator", ".")
format_thousands = settings.get("format_thousands", True)
thousands_separator = settings.get("thousands_separator", ",")

class FormatNumberCommand(sublime_plugin.TextCommand):
  def expand_region_to_whitespace(self, region):
    # Consider only the lines containing the region
    line_region = self.view.line(region)

    if not line_region:
      return None

    line_string = self.view.substr(line_region)

    # Looks for a whitespace boundary at the beginning of the region or between
    # the beginning of the region and the beginning of the line it starts on
    region_begin = region.begin() - line_region.begin()

    space_boundary_begin = self.get_space_boundary_begin(line_string,
                                                         region_begin)

    # Looks for whitespace between end of the region
    # and the end of the line it ends on
    region_end = region.end() - line_region.begin()

    space_boundary_end = self.get_space_boundary_end(line_string, region_end)

    # Returns region expanded to whitespace boundaries
    expanded_region_begin = line_region.begin() + space_boundary_begin
    expanded_region_end = line_region.begin() + space_boundary_end

    return sublime.Region(expanded_region_begin, expanded_region_end)

  def get_space_boundary_begin(self, str, pos):
    """
    Returns position of the closest whitespace boundary between `pos`
    and the beginning of the string
    """

    match = re.search(r"\S+$", str[:pos], re.UNICODE)

    if match:
      return pos - (match.end() - match.start())

    # Sets `pos` as the boundary when `str` is not preceded by a whitespace
    return pos

  def get_space_boundary_end(self, str, pos):
    """
    Returns position of the closest whitespace boundary between `pos`
    and the end of the string
    """

    match = re.search(r"\s", str[pos:], re.UNICODE)

    if match:
      return pos + match.start()

    return len(str)

  def is_number(self, str):
    """
    Strips off all locale characters from string and tests whether it's a number
    """
    result = False
    str = str.replace(decimal_separator, ".").replace(thousands_separator, "")

    try:
      val = float(str)
      result = True

    except:
      pass

    return result

  def run(self, edit):
    expanded_regions = []
    selected_regions = self.view.sel()

    # Expands selected regions to the nearest whitespace
    for region in selected_regions:
      expanded_region = self.expand_region_to_whitespace(region)

      if expanded_region is None:
        continue

      if self.is_number(self.view.substr(expanded_region)):
        expanded_regions.append(expanded_region)

    # Formats the numbers in the selected regions
    for region in reversed(expanded_regions):
      substr = self.view.substr(region)

      if thousands_separator in substr:
        # Removes formatting from the number
        new_string = substr.replace(thousands_separator, "")

      else:
        decimal_number = ""

        # Adds formatting to the number
        if bool(re.search(re.escape(decimal_separator) + '\d', substr)):
          # Splits the number into whole and decimal number strings
          whole_number, decimal_number = substr.split(decimal_separator)

        else:
          whole_number = substr

        # Skips formatting four-digit numbers when set
        if (not format_thousands) and (1000 <= int(whole_number) <= 9999):
          continue

        new_string = ""

        # Decorates whole number strings by adding a comma to every third
        # character starting from the end:
        for idx, character in enumerate(reversed(whole_number)):
          if idx % 3 == 0 and idx > 0:
            character = character + thousands_separator

          new_string = character + new_string

        # Recombines the whole and decimal number strings into a single number
        if len(decimal_number) > 0:
          new_string += decimal_separator + decimal_number

      self.view.replace(edit, region, new_string)
