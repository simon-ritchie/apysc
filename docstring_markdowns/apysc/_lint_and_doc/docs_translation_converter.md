# `apysc._lint_and_doc.docs_translation_converter` docstrings

## Module summary

This module is for the translation conversion of the documents.

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

## `_TranslationMappingNotFound` class docstring