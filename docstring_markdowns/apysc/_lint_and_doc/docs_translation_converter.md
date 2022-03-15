# `apysc._lint_and_doc.docs_translation_converter` docstrings

## Module summary

This module is for the translation conversion of the documents.

## `_add_heading_info_if_exists` function docstring

Add a target language's heading information text to a specified translated text.<hr>

**[Parameters]**

- `translated_doc`: str
  - A target translated document's text.
- `lang`: Lang
  - A target language.
- `md_file_path`: str
  - A target source document path.

<hr>

**[Returns]**

- `translated_doc`: str
  - A result translated document's text. This interface directly returns argument value if there is no heading information setting.

## `_append_double_line_breaks_if_txt_is_not_blank` function docstring

Append double line breaks if a specified text is not a blank string.<hr>

**[Parameters]**

- `txt`: str
  - A target text.

<hr>

**[Returns]**

- `txt`: str
  - A result text.

## `_apply_mapping_if_translated_str_is_api_sig` function docstring

Apply an API signature translation mapping if a specified translated string is a signature string.<hr>

**[Parameters]**

- `translated_str`: str
  - A target tlanslated string.
- `lang`: Lang
  - A target language.

<hr>

**[Returns]**

- `translated_str`: str
  - An applied string. This interface returns an argument value if a specified translated string is not a signature string.

## `_get_first_spaces_num` function docstring

Get a first spaces number of a specified string.<hr>

**[Parameters]**

- `txt`: str
  - A target string.

<hr>

**[Returns]**

- `first_spaces_num`: int
  - A first spaces number.

## `_get_sharp_heading_symbol_num` function docstring

Get a sharp heading symbol number from a specified string.<hr>

**[Parameters]**

- `target_str`: str
  - A target string to check.

<hr>

**[Returns]**

- `sharp_symbol_num`: int
  - - A sharp heading symbol number.

## `_remove_line_break_between_api_docs_list_br_tag` function docstring

Remove a line break between an API docs list's break tag.<hr>

**[Parameters]**

- `translated_doc`: str
  - A translated string.

<hr>

**[Returns]**

- `translated_doc`: str
  - A result string.

## `_remove_unnecessary_line_break_between_list` function docstring

Remove an unnecessary line break between each markdown's list.<hr>

**[Parameters]**

- `translated_doc`: str
  - A target translated document to remove an unnecessary line break.

<hr>

**[Returns]**

- `result_translated_doc`: str
  - A target translated document to remove an unnecessary line break.

## `_validate_first_br_tags_and_list_symbols_are_same` function docstring

Validate whether a string's first break tags and list symbols（・） are the same between a source string and a key string.<hr>

**[Parameters]**

- `translated_str`: str
  - A translated string.
- `key`: str
  - A key (source) string.
- `md_file_path`: str
  - A source markdown file path.

<hr>

**[Raises]**

- _BrTagsAndListSymbolsAreNotSame: This interface makes an exception if specified strings' first break tags and list symbols are not the same.

## `_validate_first_full_width_list_symbols_are_same` function docstring

Validate whether specified first full-width list symbols are the same or not.<hr>

**[Parameters]**

- `translated_str`: str
  - A translated string.
- `key`: str
  - A key (source) string.
- `md_file_path`: str
  - A source markdown file path.

<hr>

**[Raises]**

- _FirstFullWidthListSymbolsAreNotSame: If specified strings' first full-width list symbols are not the same.

## `_validate_first_spaces_nums_are_same` function docstring

Validate whether first spaces numbers are the same between a source markdown and a translated markdown text.<hr>

**[Parameters]**

- `translated_str`: str
  - A translated string.
- `key`: str
  - A key (source) string.
- `md_file_path`: str
  - A source markdown file path.

<hr>

**[Raises]**

- _FirstSpacesNumAreDifferent: This interface raises an exception if first spaces numbers are different.

## `_validate_markdown_list_hyphen_symbols_are_same` function docstring

Validate whether markdown's first hyphen symbols are the same or not.<hr>

**[Parameters]**

- `translated_str`: str
  - A translated string.
- `key`: str
  - A key (source) string.
- `md_file_path`: str
  - A source markdown file path.

<hr>

**[Raises]**

- _MarkdownListHyphenSymbolsAreNotSame: This interface makes an exception if markdown's first hyphen symbols are not the same.

## `_validate_sharp_heading_symbol_num_are_same` function docstring

Validate whether a sharp heading symbol of source and translated string are the same.<hr>

**[Parameters]**

- `translated_str`: str
  - A translated string.
- `key`: str
  - A key (source) string.
- `md_file_path`: str
  - A source markdown file path.

<hr>

**[Raises]**

- _InvalidHeadingSharpSymbolNumber: The symbol number is different for a specified translated string and a source string's sharp symbol heading.

## `_validate_tail_hr_tag` function docstring

Validate whether a tail of translated string's `<hr>` tag is valid or not.<hr>

**[Parameters]**

- `translated_str`: str
  - A translated string.
- `key`: str
  - A key (source) string.
- `md_file_path`: str
  - A source markdown file path.

<hr>

**[Raises]**

- _InvalidTailsHrTag: This interface makes an exception if a tail of a source text is the `<hr>` tag and a translated string is not.

## `_validate_translated_str_is_not_blank` function docstring

Validate whether a translated string is not a blank string.<hr>

**[Parameters]**

- `translated_str`: str
  - A target translated string.
- `key`: str
  - A target key string (original source text).
- `md_file_path`: str
  - A source markdown file path.

<hr>

**[Raises]**

- _TranslationMappingNotFound: If a specified translated string is a blank string.

## `apply_translation_to_doc` function docstring

Apply a translation mapping to a specified markdown document. This interface saves a translated file with a file name with a language suffix (e.g., jp_your_doc.md).<hr>

**[Parameters]**

- `md_file_path`: str
  - A source markdown file path.
- `lang`: Lang
  - A target language setting.

<hr>

**[Returns]**

- `translated_file_path`: str
  - A translated document file path.

## `_BrTagsAndListSymbolsAreNotSame` class docstring

## `_FirstFullWidthListSymbolsAreNotSame` class docstring

## `_FirstSpacesNumAreDifferent` class docstring

## `_InvalidHeadingSharpSymbolNumber` class docstring

## `_InvalidTailsHrTag` class docstring

## `_MarkdownListHyphenSymbolsAreNotSame` class docstring

## `_TranslationMappingNotFound` class docstring