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