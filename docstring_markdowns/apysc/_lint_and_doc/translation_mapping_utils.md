# `apysc._lint_and_doc.translation_mapping_utils` docstrings

## Module summary

This module is for translation-mapping utility implementations.

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