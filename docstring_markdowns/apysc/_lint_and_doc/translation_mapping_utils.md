# `apysc._lint_and_doc.translation_mapping_utils` docstrings

## Module summary

This module is for translation-mapping utility implementations.

## `_append_body_text_keys_to_list` function docstring

Append document's body text keys to a specified key's list.<hr>

**[Parameters]**

- `key`: str
  - A target key string. This interface splits its string if there are two consecutive line breaks.
- `keys`: list of str
  - A key's list to append.

## `_extend_keys_with_api_docs_br_tags_list` function docstring

Extend a specified keys list with an API docs' break tags list.<hr>

**[Parameters]**

- `keys`: list of str
  - A keys list to extend.
- `key_`: str
  - An API docs' break tags list string.

## `_key_is_api_docs_br_tags_list` function docstring

Get a boolean indicating whether a specified key's string is a list markdown with break tags.<hr>

**[Parameters]**

- `key_`: str
  - A target key string to check.

<hr>

**[Returns]**

- `result`: bool
  - A boolean indicates whether a specified key's string is a markdown of a list with break tags or not.

## `_key_is_api_docs_list` function docstring

Get a boolean indicating whether a specified key's string is an API document's (parameters, returns, exceptions, references) list.<hr>

**[Parameters]**

- `key_`: str
  - A target key string to check.

<hr>

**[Returns]**

- `result`: bool
  - This interface returns True if a specified key string is an API document's list.

## `convert_splitted_values_to_keys` function docstring

Convert specified splitted values to dictionary's key strings.<hr>

**[Parameters]**

- `splitted_values`: List of Heading, BodyText and CodeBlock
  - Target splitted values.

<hr>

**[Returns]**

- `keys`: list of str
  - Converted strings.

## `escape_key_or_value` function docstring

Escape a mapping key or value to save.<hr>

**[Parameters]**

- `key_or_val`: str
  - A target key or value.

<hr>

**[Returns]**

- `key_or_val`: str
  - An escaped key or value string.

## `get_hash_type_from_lang` function docstring

Get a hash type from a specified language type.<hr>

**[Parameters]**

- `lang`: Lang
  - A target translation language.

<hr>

**[Returns]**

- `hash_type`: HashType
  - A target hash type.

<hr>

**[Raises]**

- ValueError: If there is no implementation of a specified language type's branch condition.

## `get_mapping_module_path` function docstring

Get a mapping data module path.<hr>

**[Parameters]**

- `src_doc_file_path`: str
  - A target source document file path.
- `lang`: Lang
  - A target translation language.

<hr>

**[Returns]**

- `mapping_module_path`: str
  - A mapping data module path.

## `get_translated_file_path_from_src_path` function docstring

Get a translated file path from a specified source document's file path.<hr>

**[Parameters]**

- `source_doc_path`: str
  - A target document's file path.
- `lang`: Lang
  - A target language.

<hr>

**[Returns]**

- `translated_file_path`: str
  - A translated file path.

## `is_mapping_unnecessary_key` function docstring

Get a boolean indicating whether a specified key is an unnecessary mapping pattern or not.<hr>

**[Parameters]**

- `key`: str
  - A target key string to check.

<hr>

**[Returns]**

- `result`: bool
  - This interface returns True if a specified key is an unnecessary mapping pattern.

## `is_translation_skipping_key` function docstring

Get a boolean indicating whether a specified key is a translation skipping pattern or not.<hr>

**[Parameters]**

- `key`: str
  - A target key string to check.

<hr>

**[Returns]**

- `result`: bool
  - This interface returns True if a specified key is a translation skipping pattern.

## `read_mapping_data` function docstring

Read an already saved mapping data.<hr>

**[Parameters]**

- `src_doc_file_path`: str
  - A target source document file path.
- `lang`: Lang
  - A target translation language.

<hr>

**[Returns]**

- `already_saved_mapping`: dict
  - An already saved mapping data dictionary.

## `remove_empty_keys` function docstring

Remove empty (or only spaces) keys (source text) from a specified list.<hr>

**[Parameters]**

- `keys`: list of str
  - A target keys list.

<hr>

**[Returns]**

- `result_keys`: list of str
  - A result keys list.

## `remove_escaping_from_key_or_value` function docstring

Remove escaping characters from a specified key or value string.<hr>

**[Parameters]**

- `key_or_val`: str
  - A target key or value string.

<hr>

**[Returns]**

- `key_or_val`: str
  - A result key or value string.