# `apysc._lint_and_doc.fixed_translation_mapping.data_model` docstrings

## Module summary

This module is for the data model of the fixed-translation mapping settings.

## `_get_mappings_module_path_from_lang` function docstring

Get a fixed-translation mappings settings module path of a specified language.<hr>

**[Parameters]**

- `lang`: Lang
  - A target language.

<hr>

**[Returns]**

- `module_path`: str
  - A fixed-translation mappings settings module path of a specified language.

## `get_fixed_translation_str_if_exists` function docstring

Get a fixed-translation string from a specified language key string if there is a mapping setting.<hr>

**[Parameters]**

- `key`: str
  - A target key string (source english string).
- `lang`: Lang
  - A target language.

<hr>

**[Returns]**

- `translation_str`: str
  - A translated string. If there is no fixed-translation mapping setting, this interface returns a blank string.

## `Mapping` class docstring

The class of a single fixed-translation mapping settings.

### `__init__` method docstring

A single fixed-translation mapping settings.<hr>

**[Parameters]**

- `key`: str
  - A key value (this value needs to set a source english string).
- `value`: str
  - A translated value.

## `Mappings` class docstring

The class for fixed-translation mappings settings.

### `__init__` method docstring

The class for fixed-translation mappings settings.<hr>

**[Parameters]**

- `mappings`: list of Mapping
  - A target mappings list.