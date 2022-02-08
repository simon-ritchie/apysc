# apysc._string.string_util docstrings

## Module summary

Common string utilities. Mainly following interfaces and defined. <br>・escape_str Escape special characters (e.g. line breaks of ` `). <br>・escape_double_quotation Escape double quotations. <br>・wrap_by_double_quotation_if_value_is_string Wrap specified by double quotation if value is a string. <br>・substitute_file_by_pattern Substitute text file by regular expression pattern. <br>・replace_double_spaces_to_single_space Replace double spaces to a single space.

## escape_double_quotation function docstring

Escape double quotations.<hr>

**[Parameters]**

- `string`: str
  - String to escape.

<hr>

**[Returns]**

- `string`: str
  - Escaped string.

## escape_str function docstring

Escape special characters (e.g. line breaks of ` `).<hr>

**[Parameters]**

- `string`: str
  - String to escape.

<hr>

**[Returns]**

- `string`: str
  - Escaped string.

## replace_double_spaces_to_single_space function docstring

Replace double spaces to a single space.<hr>

**[Parameters]**

- `string`: str
  - Target string to replace.

<hr>

**[Returns]**

- `string`: str
  - Replaced string.

## substitute_file_by_pattern function docstring

Substitute text file by regular expression pattern.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.
- `pattern`: str
  - Regular expression pattern.
- `repl`: str
  - String that replace matched pattern one.
- `flags`: Any
  - Regular expression flags.

## wrap_by_double_quotation_if_value_is_string function docstring

Wrap specified by double quotation if value is a string.<hr>

**[Parameters]**

- `value`: *
  - Any value to wrap.

<hr>

**[Returns]**

- `value`: *
  - Wrapped value. If not string value is specified, return that value imediatelly.

## TypeVar class docstring

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

Type variable. Usage:: T = TypeVar('T') # Can be anything A = TypeVar('A', str, bytes) # Must be str or bytes Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions. See class Generic for more information on generic types. Generic functions work as follows: def repeat(x: T, n: int) -> List[T]: '''Return a list containing n references to x.''' return [x]*n def longest(x: A, y: A) -> A: '''Return the longest of two strings.''' return x if len(x) >= len(y) else y The latter example's signature is essentially the overloading of (str, str) -> str and (bytes, bytes) -> bytes. Also note that if the arguments are instances of some subclass of str, the return type is still plain str. At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError. Type variables defined with covariant=True or contravariant=True can be used do declare covariant or contravariant generic types. See PEP 484 for more details. By default generic types are invariant in all type variables. Type variables can be introspected. e.g.: T.__name__ == 'T' T.__constraints__ == () T.__covariant__ == False T.__contravariant__ = False A.__constraints__ == (str, bytes)

### TypingMeta method docstring

Metaclass for most types defined in typing module (not a part of public API). This overrides __new__() to require an extra keyword parameter '_root', which serves as a guard against naive subclassing of the typing classes. Any legitimate class defined using a metaclass derived from TypingMeta must pass _root=True. This also defines a dummy constructor (all the work for most typing constructs is done in __new__) and a nicer repr().

### __new__ method docstring

Constructor. This only exists to give a better error message in case someone tries to subclass a special typing object (not a good idea).