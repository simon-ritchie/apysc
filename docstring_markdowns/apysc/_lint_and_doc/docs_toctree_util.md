# `apysc._lint_and_doc.docs_toctree_util` docstrings

## Module summary

The utility module for the documents toctree.

## `_extract_toctree_file_names_from_file` function docstring

Extract toctree file names from a specified file.<hr>

**[Parameters]**

- `toctree_defined_en_file_name`: str
  - An English document file name that contains the toctree definition.

<hr>

**[Returns]**

- `toctree_file_names`: List[str]
  - Extracted toctree file names.

## `_get_expected_next_md_file_name` function docstring

Get an expected next markdown file name from a specified index and list.<hr>

**[Parameters]**

- `toctree_file_names`: List[str]
  - A list of markdown file names.
- `i`: int
  - Target list index.

<hr>

**[Returns]**

- `expected_next_md_file_name`: str
  - An expected next markdown file name.

## `_get_expected_prev_md_file_name` function docstring

Get an expected previous markdown file name from a specified index and list.<hr>

**[Parameters]**

- `toctree_file_names`: List[str]
  - A list of markdown file names.
- `i`: int
  - Target list index.

<hr>

**[Returns]**

- `expected_prev_md_file_name`: str
  - An expected previous markdown file name.

## `_update_adjacent_doc_modified_time_if_toctree_updated` function docstring

Update a specified adjacent document's modified time if a related toctree differs from an expected file name.<hr>

**[Parameters]**

- `adjacent_doc_file_name`: str
  - An adjacent document file name.
- `expected_md_file_name`: str
  - An expected document file name.

<hr>

**[Returns]**

- `is_updated`: bool
  - A boolean indicates whether this function updated an adjacent document's modified time or not.

## `get_doc_prev_and_next_md_file_names` function docstring

Get specified markdown file's previous and next markdown file names.<hr>

**[Parameters]**

- `md_doc_file_name`: str
  - Target markdown file name (e.g., sprite.md).

<hr>

**[Returns]**

- `prev_md_doc_file_name`: str
  - A previous markdown file name.
- `next_md_doc_file_name`: str
  - A next markdown file name.

## `get_toctree_file_names` function docstring

Get toctree file names from the toctree defined files.<hr>

**[Returns]**

- `toctree_file_names`: List[str]
  - Result toctree file names (e.g., ["what_apysc_can_do.md", "quick_start.md", ...]).

## `update_docs_prev_and_next_page_modified_time` function docstring

Update documents next and previous pages' modified time.