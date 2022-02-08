# apysc._lint_and_doc.docstring_util docstrings

## Module summary

Utility implementations for docstrings.

## _append_br_tag_and_replace_symbol_if_first_char_is_hyphen function docstring

Append a break tag and replace the hypen symbol if the first character is the hypen symbol.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `line`: str
  - Replaced docstring line.

## _convert_docstring_path_comment_to_markdown_format function docstring

Convert a specified docstring path comment to a markdown format text.<hr>

**[Parameters]**

- `docstring_path_comment`: str
  - Target docstring path comment.
- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `markdown_format_docstring`: str
  - Converted text.

## _convert_docstring_to_markdown function docstring

Convert a specified docstring to a markdown format text.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.
- `signature`: Signature or None
  - Target callable's signature. If a target interface is property, this argument becomes None.
- `callable_name`: str
  - Target callable name.
- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `markdown`: str
  - Converted markdown text.

## _extract_docstring_path_specification_comment_from_line function docstring

Extract a docstring path specification comment from a specified markdown line text.<hr>

**[Parameters]**

- `line`: str
  - Target markdown line text.
- `matches`: list of str
  - Matched docstring path specification comments.

<hr>

**[Returns]**

- `docstring_path_specification_comment`: str
  - Extracted comment string.

## _extract_package_path_and_callable_name_from_path function docstring

Extract a module or class package path and callable name from a specified path comment.<hr>

**[Parameters]**

- `docstring_path_comment`: str
  - Target docstring path comment.

<hr>

**[Returns]**

- `module_or_class_package_path`: str
  - Extracted module or class package path. e.g., 'apy.path' or 'any.path.AnyClass'.
- `callable_name`: str
  - Extracted callable name.

## _extract_path_from_docstring_comment function docstring

Extract a path string from a specified docstring path comment.<hr>

**[Parameters]**

- `docstring_path_comment`: str
  - Target docstring path comment.

<hr>

**[Returns]**

- `path`: str
  - Extracted path string.

## _get_base_indent_num_if_not_set function docstring

Get a base indent number from line if it is not set.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.
- `base_indent_num`: int
  - Current base indent number.

<hr>

**[Returns]**

- `base_indent_num`: int
  - If the base_indent_num argument is zero, this function returns the current line indent number. Otherwise, it returns the same value of the base_indent_num argument.

## _get_callable_from_package_path_and_callable_name function docstring

Get a callable object from a specified package path and callable name.<hr>

**[Parameters]**

- `module_or_class_package_path`: str
  - Target module or class package path.
- `callable_name`: str
  - Target callable name.

<hr>

**[Returns]**

- `callable_`: Callable
  - Target callable object.

<hr>

**[Raises]**

- _DocstringPathNotFoundError: If a specified package path's module or class does not exist.
- _DocstringCallableNotExistsError: If a target module or class does not have a specified name function or method.

## _get_docstring_path_comment_matches function docstring

Get matched docstring path specification comments.<hr>

**[Parameters]**

- `md_txt`: str
  - Target markdown text.

<hr>

**[Returns]**

- `matches`: list of str
  - Matched comments.

## _get_indent_num_from_line function docstring

Get an indent number from a specified docstring line.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `indent_num`: int
  - Indent number of a specified docstring line.

## _get_params_or_rtns_section_pattern_by_type function docstring

Get the parameters or returns section pattern of a specified type.<hr>

**[Parameters]**

- `target_type`: Parameter or Return
  - Target type.

<hr>

**[Returns]**

- `pattern`: _SectionPattern
  - Target section pattern.

<hr>

**[Raises]**

- ValueError: If an invalid target type is provided.

## _get_value_name_and_type_from_line function docstring

Get a parameter or return value and type from a specified line.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `value_name`: str
  - Target parameter or return value name.
- `type_name`: str
  - Target parameter or return value type name.

## _is_example_output_line function docstring

Get a boolean indicating whether a specified line is example section's output line or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `result`: bool
  - This function return True if a specified line is example section's output line.

## _is_hyphens_line function docstring

Get a boolean indicating whether a specified line is a hyphens line or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `result`: bool
  - If a specified line is a hyphens line, this function returns True.

## _is_section_line function docstring

Get a boolean indicating whether a specified docstring line is a section line or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line text.

<hr>

**[Returns]**

- `result`: bool
  - If a specified docstring line is section line, this function returns True.

## _is_skip_target_line function docstring

Get a boolean indicating whether a specified line is skipping target or not.<hr>

**[Parameters]**

- `is_target_section_range`: bool
  - A boolean indicating whether a specified line is in a range of target section.
- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `result`: bool
  - A boolean indicating whether a specified line is skipping target or not.

## _is_target_section_pattern_line function docstring

Get a boolean indicating whether a specified line is matching with a target section pattern or not.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.
- `section_pattern`: _SectionPattern
  - Target section pattern.

<hr>

**[Returns]**

- `result`: bool
  - If a specified line is the parameters section, this function returns True.

## _make_example_and_append_to_list function docstring

Make an example value and append it ot a specified list.<hr>

**[Parameters]**

- `example_values`: list of Example
  - A list to append an example value.
- `input_code_block_lines`: list of str
  - A list of input code block lines.
- `expected_output`: str
  - An expected output string.

<hr>

**[Notes]**

This function clears a list of input code block lines.

## _make_prm_or_rtn_description_and_append_to_list function docstring

Make a parameter or return value description from a list of lines and append parameter or return value to a specified list.<hr>

**[Parameters]**

- `target_type`: Type
  - Target type of the Parameter or Return.
- `param_or_rtn_values`: lisf of _ParamOrRtnBase
  - A list to append a parameter or return value.
- `value_name`: str
  - Parameter or return value name.
- `value_type_str`: str
  - Parameter or return type name.
- `description_lines`: list of str
  - A list of description lines.

<hr>

**[Notes]**

This function clears a list of description lines.

## _make_raise_description_and_append_to_list function docstring

Make a raise value description from a list of lines and append raise value to a specified list.<hr>

**[Parameters]**

- `raise_values`: list of Raise
  - A list to append a raise value.
- `err_class_name`: str
  - Target error class name.
- `description_lines`: list of str
  - A list of description lines.

<hr>

**[Notes]**

This function clears a list of description lines.

## _make_reference_and_append_to_list function docstring

Make a reference value and append it to a specified list.<hr>

**[Parameters]**

- `reference_values`: list of Reference
  - A list to append a reference value.
- `page_label`: str
  - Target reference page label.
- `url`: str
  - Target reference page URL.

## _remove_blank_lines_from_list function docstring

Remove blank lines from a list of lines.<hr>

**[Parameters]**

- `lines`: list of str
  - Target list of lines.

<hr>

**[Returns]**

- `result_lines`: list of str
  - A lines list which removed blank lines.

## _remove_line_breaks_and_unnecessary_spaces function docstring

Remove line breaks to a single space and unnecessary spaces (e.g., double spaces and leading and trailing spaces).<hr>

**[Parameters]**

- `text`: str
  - Target text.

<hr>

**[Returns]**

- `text`: str
  - Converted text.

## _remove_noqa function docstring

Remove a noqa comment from a specified string.<hr>

**[Parameters]**

- `string`: str
  - Target string.

<hr>

**[Returns]**

- `string`: str
  - Result string.

## _remove_replaced_docstring_section_from_md_txt function docstring

Remove replaced docstring from a specified markdown text.<hr>

**[Parameters]**

- `md_txt`: str
  - Target markdown text.
- `matches`: list of str
  - Matched docstring path specification comments.

<hr>

**[Returns]**

- `md_txt`: str
  - Result markdown text.

## _remove_unnecessary_markdown_list_from_line function docstring

Remove unnecessary markdown list string from a line.<hr>

**[Parameters]**

- `line`: str
  - Target docstring line.

<hr>

**[Returns]**

- `line`: str
  - Result docstring line.

## _slice_references_by_md_file_path function docstring

Slice a specified references list to exclude a same URL's document file.<hr>

**[Parameters]**

- `references`: list of Reference
  - Target references list to slice.
- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `sliced_references`: list of Reference
  - Sliced list.

## append_examples_to_markdown function docstring

Append examples to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `examples`: list of Example
  - Examples list value to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## append_notes_to_markdown function docstring

Append a notes string to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `notes`: str
  - Target notes string.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## append_params_or_rtns_to_markdown function docstring

Append parameters or returns to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `params_or_rtns`: list of _ParamOrRtn
  - Parameters or returns to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## append_raises_to_markdown function docstring

Append raises to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `raises`: list of Raise
  - Raises list value to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## append_references_to_markdown function docstring

Append references to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `references`: list of Reference
  - References list value to append to.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## append_summary_to_markdown function docstring

Append a interface summary string to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `summary`: str
  - Target summary string.
- `heading_label`: str
  - A label to append at the beginning.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## extract_example_values_from_docstring function docstring

Extract example values from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `example_values`: list of Example
  - Extracted example values.

## extract_notes_from_docstring function docstring

Extract a notes value from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `notes`: str
  - Extract notes text value.

## extract_param_or_rtn_values_from_docstring function docstring

Extract parameter or return values from a docstring.<hr>

**[Parameters]**

- `target_type`: Type
  - Target type of the Parameter or Return.
- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `param_or_rtn_values`: list of Parameter or Return
  - Extracted parameter or return values.

## extract_raise_values_from_docstring function docstring

Extract raise values from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `raise_values`: list of Raise
  - Extracted raise values.

## extract_reference_values_from_docstring function docstring

Extract reference values from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `reference_values`: list of Reference
  - Extracted reference values.

## extract_summary_from_docstring function docstring

Extract a summary text from a docstring.<hr>

**[Parameters]**

- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `summary`: str
  - Extracted summary text.

<hr>

**[Notes]**

This function converts line break to a space.

## get_docstring_src_module_paths function docstring

Get docstring source module paths from a specified markdown file path.<hr>

**[Parameters]**

- `md_file_path`: str
  - Target markdown file path.

<hr>

**[Returns]**

- `module_paths`: list of str
  - Extracted docstring source module paths.

## remove_trailing_hr_tag function docstring

Remove a trailing `<hr>` tag from a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.

<hr>

**[Returns]**

- `markdown`: str
  - Result markdown string.

## replace_docstring_path_specification function docstring

Replace a docstring path specification in a specified markdown document by a converted docstring text.<hr>

**[Parameters]**

- `md_file_path`: str
  - Target markdown file path.

## reset_replaced_docstring_section function docstring

Reset converted a markdown's docstring section.<hr>

**[Parameters]**

- `md_file_path`: str
  - Target markdown document file path.

<hr>

**[Returns]**

- `is_executed`: bool
  - Replacing is executed or not.

## Callable class docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

### CallableMeta method docstring

Metaclass for Callable (internal).

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### object method docstring

The most base type

### Callable method docstring

Callable type; Callable[[int], str] is a function of (int) -> str. The subscription syntax must always be used with exactly two values: the argument list and the return type. The argument list must be a list of types or ellipsis; the return type must be a single type. There is no syntax to indicate optional or keyword arguments, such function types are rarely used as callback types.

## Enum class docstring

Generic enumeration. Derive from this class to define new enumerations.

Generic enumeration. Derive from this class to define new enumerations.

### EnumMeta method docstring

Metaclass for Enum

## Example class docstring

Example value type.

Example value type.

### __eq__ method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### __init__ method docstring

Example value type.<hr>

**[Parameters]**

- `input_code_block`: str
  - Input code block string.
- `expected_output`: str, default ''
  - Expected output string.

## List class docstring



### __add__ method docstring

Return self+value.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __contains__ method docstring

Return key in self.

### __delitem__ method docstring

Delete self[key].

### list method docstring

list() -> new empty list list(iterable) -> new list initialized from iterable's items

### __getitem__ method docstring

x.__getitem__(y) <==> x[y]

### __iadd__ method docstring

Implement self+=value.

### __imul__ method docstring

Implement self*=value.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mul__ method docstring

Return self*value.

### object method docstring

The most base type

### __reversed__ method docstring

L.__reversed__() -- return a reverse iterator over the list

### __rmul__ method docstring

Return value*self.

### __setitem__ method docstring

Set self[key] to value.

### __sizeof__ method docstring

L.__sizeof__() -- size of L in memory, in bytes

### append method docstring

L.append(object) -> None -- append object to end

### clear method docstring

L.clear() -> None -- remove all items from L

### copy method docstring

L.copy() -> list -- a shallow copy of L

### count method docstring

L.count(value) -> integer -- return number of occurrences of value

### extend method docstring

L.extend(iterable) -> None -- extend list by appending elements from the iterable

### index method docstring

L.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

### insert method docstring

L.insert(index, object) -- insert object before index

### pop method docstring

L.pop([index]) -> item -- remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.

### remove method docstring

L.remove(value) -> None -- remove first occurrence of value. Raises ValueError if the value is not present.

### reverse method docstring

L.reverse() -- reverse *IN PLACE*

### sort method docstring

L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

## Parameter class docstring

Parameter value type.

Parameter value type.

### __eq__ method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other instance to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### __init__ method docstring

Parameter or return value's base class.<hr>

**[Parameters]**

- `name`: str
  - Parameter or return value name.
- `type_str`: str
  - Parameter or return value type name.
- `description`: str
  - Parameter or return value description.

## Raise class docstring

Raise value type.

Raise value type.

### __eq__ method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### __init__ method docstring

Raise value type.<hr>

**[Parameters]**

- `err_class_name`: str
  - Target error class name.
- `description`: str
  - Error condition description.

## Reference class docstring

Reference value type.

Reference value type.

### __eq__ method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### __init__ method docstring

Reference value type.<hr>

**[Parameters]**

- `page_label`: str
  - Target reference page label.
- `url`: str
  - Target reference page URL.

## Return class docstring

Return value type.

Return value type.

### __eq__ method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other instance to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### __init__ method docstring

Parameter or return value's base class.<hr>

**[Parameters]**

- `name`: str
  - Parameter or return value name.
- `type_str`: str
  - Parameter or return value type name.
- `description`: str
  - Parameter or return value description.

## Signature class docstring

A Signature object represents the overall signature of a function. It stores a Parameter object for each parameter accepted by the function, as well as information specific to the function itself. A Signature object has the following public attributes and methods: * parameters : OrderedDict An ordered mapping of parameters' names to the corresponding Parameter objects (keyword-only arguments are in the same order as listed in `code.co_varnames`). * return_annotation : object The annotation for the return type of the function if specified. If the function has no annotation for its return type, this attribute is set to `Signature.empty`. * bind(*args, **kwargs) -> BoundArguments Creates a mapping from positional and keyword arguments to parameters. * bind_partial(*args, **kwargs) -> BoundArguments Creates a partial mapping from positional and keyword arguments to parameters (simulating 'functools.partial' behavior.)

A Signature object represents the overall signature of a function. It stores a Parameter object for each parameter accepted by the function, as well as information specific to the function itself. A Signature object has the following public attributes and methods: * parameters : OrderedDict An ordered mapping of parameters' names to the corresponding Parameter objects (keyword-only arguments are in the same order as listed in `code.co_varnames`). * return_annotation : object The annotation for the return type of the function if specified. If the function has no annotation for its return type, this attribute is set to `Signature.empty`. * bind(*args, **kwargs) -> BoundArguments Creates a mapping from positional and keyword arguments to parameters. * bind_partial(*args, **kwargs) -> BoundArguments Creates a partial mapping from positional and keyword arguments to parameters (simulating 'functools.partial' behavior.)

### __init__ method docstring

Constructs Signature from the given list of Parameter objects and 'return_annotation'. All arguments are optional.

### _bind method docstring

Private method. Don't use directly.

### BoundArguments method docstring

Result of `Signature.bind` call. Holds the mapping of arguments to the function's parameters. Has the following public attributes: * arguments : OrderedDict An ordered mutable mapping of parameters' names to arguments' values. Does not contain arguments' default values. * signature : Signature The Signature object that created this instance. * args : tuple Tuple of positional arguments values. * kwargs : dict Dict of keyword arguments values.

### Parameter method docstring

Represents a parameter in a function signature. Has the following public attributes: * name : str The name of the parameter as a string. * default : object The default value for the parameter if specified. If the parameter has no default value, this attribute is set to `Parameter.empty`. * annotation The annotation for the parameter if specified. If the parameter has no annotation, this attribute is set to `Parameter.empty`. * kind : str Describes how argument values are bound to the parameter. Possible values: `Parameter.POSITIONAL_ONLY`, `Parameter.POSITIONAL_OR_KEYWORD`, `Parameter.VAR_POSITIONAL`, `Parameter.KEYWORD_ONLY`, `Parameter.VAR_KEYWORD`.

### bind method docstring

Get a BoundArguments object, that maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

### bind_partial method docstring

Get a BoundArguments object, that partially maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

### _empty method docstring

Marker object for Signature.empty and Parameter.empty.

### from_builtin method docstring

Constructs Signature for the given builtin function. Deprecated since Python 3.5, use `Signature.from_callable()`.

### from_callable method docstring

Constructs Signature for the given callable object.

### from_function method docstring

Constructs Signature for the given python function. Deprecated since Python 3.5, use `Signature.from_callable()`.

### replace method docstring

Creates a customized copy of the Signature. Pass 'parameters' and/or 'return_annotation' arguments to override them in the new copy.

## Tuple class docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### __add__ method docstring

Return self+value.

### TupleMeta method docstring

Metaclass for Tuple (internal).

### __contains__ method docstring

Return key in self.

### tuple method docstring

tuple() -> empty tuple tuple(iterable) -> tuple initialized from iterable's items If the argument is a tuple, the return value is the same object.

### __getitem__ method docstring

Return self[key].

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### __iter__ method docstring

Implement iter(self).

### __len__ method docstring

Return len(self).

### __mul__ method docstring

Return self*value.

### object method docstring

The most base type

### __rmul__ method docstring

Return value*self.

### Tuple method docstring

Tuple type; Tuple[X, Y] is the cross-product type of X and Y. Example: Tuple[T1, T2] is a tuple of two elements corresponding to type variables T1 and T2. Tuple[int, float, str] is a tuple of an int, a float and a string. To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].

### count method docstring

T.count(value) -> integer -- return number of occurrences of value

### index method docstring

T.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.

## Type class docstring

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.

### GenericMeta method docstring

Metaclass for generic types. This is a metaclass for typing.Generic and generic ABCs defined in typing module. User defined subclasses of GenericMeta can override __new__ and invoke super().__new__. Note that GenericMeta.__new__ has strict rules on what is allowed in its bases argument: * plain Generic is disallowed in bases; * Generic[...] should appear in bases at most once; * if Generic[...] is present, then it should list all type variables that appear in other bases. In addition, type of all generic bases is erased, e.g., C[int] is stripped to plain C.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### object method docstring

The most base type

### Type method docstring

A special construct usable to annotate class objects. For example, suppose we have the following classes:: class User: ... # Abstract base for User classes class BasicUser(User): ... class ProUser(User): ... class TeamUser(User): ... And a function that takes a class argument that's a subclass of User and returns an instance of the corresponding class:: U = TypeVar('U', bound=User) def new_user(user_class: Type[U]) -> U: user = user_class() # (Here we could write the user object to a database) return user joe = new_user(BasicUser) At this point the type checker knows that joe has type BasicUser.

## TypeVar class docstring

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

### TypingMeta method docstring

Metaclass for most types defined in typing module (not a part of public API). This overrides __new__() to require an extra keyword parameter '_root', which serves as a guard against naive subclassing of the typing classes. Any legitimate class defined using a metaclass derived from TypingMeta must pass _root=True. This also defines a dummy constructor (all the work for most typing constructs is done in __new__) and a nicer repr().

### __new__ method docstring

Constructor. This only exists to give a better error message in case someone tries to subclass a special typing object (not a good idea).

## _DocstringCallableNotExistsError class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### with_traceback method docstring

Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.

## _DocstringPathNotFoundError class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### with_traceback method docstring

Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.

## _ParamOrRtnBase class docstring



### __eq__ method docstring

The method for equality comparison.<hr>

**[Parameters]**

- `other`: Any
  - Other instance to compare with.

<hr>

**[Returns]**

- `result`: bool
  - If each attribute is equal to the other, this method returns True.

### __init__ method docstring

Parameter or return value's base class.<hr>

**[Parameters]**

- `name`: str
  - Parameter or return value name.
- `type_str`: str
  - Parameter or return value type name.
- `description`: str
  - Parameter or return value description.

## _SectionPattern class docstring

An enumeration.

An enumeration.

### EnumMeta method docstring

Metaclass for Enum