# `apysc._lint_and_doc.document_text_split_util` docstrings

## Module summary

This module is for the document splitting utility.

## `_create_body_text_and_append_to_list_if_values_exist` function docstring

Create a body text instance from a specified body text lines list and append it to a result list. This interface skips the appending if a specified body text line list is blank.<hr>

**[Parameters]**

- `splitted_values`: list of Heading, BodyText, and CodeBlock
  - A result list to append a body text instance.
- `body_text_lines`: list of str
  - A target body text line's list.

<hr>

**[Notes]**

This function clears a specified body text lines list at the end.

## `_create_code_block_from_list` function docstring

Create a code block instance from a specified lines list.<hr>

**[Parameters]**

- `code_block_lines`: list of str
  - A target code block lines.

<hr>

**[Returns]**

- `code_block`: CodeBlock
  - A created code block instance.

<hr>

**[Notes]**

This function clears a specified list at the end of the function.

## `split_markdown_document` function docstring

Split a specified markdown document to `Heading`, `BodyText`, and `CodeBlock` values.<hr>

**[Parameters]**

- `markdown_txt`: str
  - A target markdown document.

<hr>

**[Returns]**

- `splitted_values`: list of Heading, BodyText, and CodeBlock
  - A list of splitted `Heading`, `BodyText`, and `CodeBlock` values.

## `BodyText` class docstring

This class is for a document body text.

### `__init__` method docstring

The class for a document body text.<hr>

**[Parameters]**

- `text`: str
  - A document body text.

## `CodeBlock` class docstring

### `__init__` method docstring

The class for a document code block.<hr>

**[Parameters]**

- `code_block`: str
  - A document code block.

## `Heading` class docstring

This class is for the document's heading.

### `__init__` method docstring

The class for the document's heading.<hr>

**[Parameters]**

- `heading_text`: str
  - A heading text of a document.