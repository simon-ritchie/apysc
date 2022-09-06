# `apysc._lint_and_doc.fixed_translation_mapping.data_model` docstrings

## Module summary

This module is for the data model of the fixed-translation mapping settings.

## `_get_fixed_mapping_hash_type` function docstring

Get a hash type for a specified language.<hr>

**[Parameters]**

- `lang`: Lang
  - Target language setting.

<hr>

**[Returns]**

- `hash_type`: HashType
  - A target hash type.

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

If a mapping setting exists, get a fixed-translation string from a specified language key string.<hr>

**[Parameters]**

- `key`: str
  - A target key string (source English string).
- `lang`: Lang
  - A target language.

<hr>

**[Returns]**

- `translation_str`: str
  - A translated string. If there is no fixed-translation mapping setting, this interface returns a blank string.

## `is_fixed_mapping_updated` function docstring

Get a boolean that indicates whether the fixed mapping's settings module has been updated.<hr>

**[Parameters]**

- `lang`: Lang
  - Target language setting.

<hr>

**[Returns]**

- `result`: bool
  - This interface returns True if the settings have been updated.

## `save_fixed_mapping_hash` function docstring

Save a fixed mapping module's hash file.<hr>

**[Parameters]**

- `lang`: Lang
  - Target language setting.

## `Mapping` class docstring

This class is for a single fixed-translation mapping setting.

### `__init__` method docstring

A single fixed-translation mapping setting.<hr>

**[Parameters]**

- `key`: str
  - A key value (this value needs to set source English string).
- `val`: str
  - A translated value.

## `Mappings` class docstring

This class is for fixed-translation mappings settings.

### `__init__` method docstring

The class for fixed-translation mappings settings.<hr>

**[Parameters]**

- `mappings`: list of Mapping
  - A target mappings list.

## `_UnsupportedLanguageException` class docstring