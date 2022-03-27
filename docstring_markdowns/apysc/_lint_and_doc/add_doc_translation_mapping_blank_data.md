# `apysc._lint_and_doc.add_doc_translation_mapping_blank_data` docstrings

## Module summary

This module is for adding document translations mapping dictionary's blank data.

## `_convert_link_list_by_lang` function docstring

Convert a link list value by a specified language if a key's value is a link list.<hr>

**[Parameters]**

- `key`: str
  - A target key string (source English string).
- `value`: str
  - A target value string.
- `lang`: Lang
  - A target translation language.

<hr>

**[Returns]**

- `value`: str
  - A converted value. This interface skips the conversion if a specified key's value is not a link list.

## `_extract_link_texts` function docstring

Extract link texts from a specified value string.<hr>

**[Parameters]**

- `value`: str
  - A target value string.

<hr>

**[Returns]**

- `link_texts`: list of str
  - Extracted link texts.

## `_get_src_docs_file_paths` function docstring

Get source documents file paths.<hr>

**[Returns]**

- `src_docs_file_paths`: list of str
  - Source documents file paths.

## `_is_translated_document` function docstring

Get a boolean indicating whether a specified document path is a translated document or not.<hr>

**[Parameters]**

- `path`: str
  - A target document path.

<hr>

**[Returns]**

- `result`: bool
  - If a specified document path is a translated document, this interface returns True.

## `_make_mappings_from_keys` function docstring

Make mapping dictionary values from specified key values.<hr>

**[Parameters]**

- `keys`: list of str
  - Target dictionary key values.
- `src_doc_file_path`: str
  - A target source document file path.
- `lang`: Lang
  - A target translation language.

<hr>

**[Returns]**

- `mappings`: list of dict
  - Created mapping dictionary values. A dictionary value becomes a blank string if it is a new mapping value.

## `_remove_skipping_pattern_keys_from_list` function docstring

Remove skipping pattern matching keys from a specified list.<hr>

**[Parameters]**

- `keys`: list of str
  - A target key's list.

<hr>

**[Returns]**

- `result_keys`: list of str
  - An after removing key's list.

## `_replace_link_text_by_fixed_mapping` function docstring

Replace each link text if there are fixed translation-mapping settings.<hr>

**[Parameters]**

- `value`: str
  - A link text.
- `lang`: Lang
  - A target translation language.

<hr>

**[Returns]**

- `value`: str
  - A replaced link text. This interface returns a blank string if there is no translation mapping.

## `_save_mapping_data` function docstring

Save mapping data module with specified mappings data.<hr>

**[Parameters]**

- `mappings`: list of dict
  - Target mappings data to save.
- `src_doc_file_path`: str
  - A target source document's file path.
- `lang`: Lang
  - A target translation language.

## `_set_fixed_translation_value_if_exists` function docstring

Set a fixed translation value if its mapping setting exists.<hr>

**[Parameters]**

- `key`: str
  - A target translation key.
- `value`: str
  - A current translation value.

<hr>

**[Returns]**

- `fixed_value`: str
  - A fixed translation value. If there is no fixed translation mapping setting, this interface directly returns an argument's value.

## `_set_same_value_if_api_params_or_returns_list` function docstring

Set the same key as a value if a specified key string is an API's parameters or returns list's line.<hr>

**[Parameters]**

- `key`: str
  - A target key string.
- `value`: str
  - A target value.

<hr>

**[Returns]**

- `value`: str
  - This interface returns a key's value if a specified key string is an API's parameters or returns line. Otherwise, this interface returns a specified value directly.

## `_set_same_value_if_code_block_mapping_is_blank` function docstring

Set the same code-block value if a specified value is a blank string and a key's value is a code block.<hr>

**[Parameters]**

- `key`: str
  - A target key string (source English string).
- `value`: str
  - A target value string.

<hr>

**[Returns]**

- `value`: str
  - A result value. If an argument value is not a blank string, this interface returns it directly. If a key's value is not a code block, this interface also returns an argument value directly.

## `_set_same_value_if_key_is_image_link` function docstring

Set the same key as a value if a specified key is an image link string with an alternative blank text.<hr>

**[Parameters]**

- `key`: str
  - A target key string.
- `value`: str
  - A target value.

<hr>

**[Returns]**

- `value`: str
  - This interface returns the same value if a specified key is an image link string with an alternative blank text. Otherwise, it returns a value argument directly.

## `_set_same_value_if_key_is_no_mapping_fixed_string` function docstring

Set the same key as a value if a specified key is a no-mapping fixed string.<hr>

**[Parameters]**

- `key`: str
  - A target key string.
- `value`: str
  - A target value.

<hr>

**[Returns]**

- `value`: str
  - This interface returns a key's value if a specified key is a no-mapping fixed string. Otherwise, this interface returns a specified value directly.

## `add_mapping_blank_data` function docstring

Add a mapping's blank data of document translations.<hr>

**[Parameters]**

- `lang`: Lang
  - A target translation language.