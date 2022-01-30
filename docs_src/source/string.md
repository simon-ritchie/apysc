# String

This page explains the `String` class.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the String class?

The `String` class is the apysc string class. It can accept `str` or `String` values at the constructor, as follows:

```py
# runnable
import apysc as ap

string_1: ap.String = ap.String('Hello')
assert string_1 == 'Hello'

string_2: ap.String = ap.String(string_1)
assert string_2 == 'Hello'
```

## String class interfaces

For more details about the `String` class each interface, please see the following:

- [String class comparison operations](string_comparison_operations.md)
- [String class addition and multiplication operations](string_addition_and_multiplication.md)


## String class constructor API

<!-- Docstring: apysc._type.string.String.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value:Union[str, _ForwardRef('String')]) -> None`<hr>

**[Interface summary]** String class for apysc library.<hr>

**[Parameters]**

- `value`: str or String
  - Initial string value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String('Hello')
>>> string
String('Hello')

>>> string += ' World!'
>>> string
String('Hello World!')
```

<hr>

**[References]**

- [String class comparison operations document](https://simon-ritchie.github.io/apysc/string_comparison_operations.html)
- [String class addition and multiplication operations document](https://simon-ritchie.github.io/apysc/string_addition_and_multiplication.html)

## value property API

<!-- Docstring: apysc._type.string.String.value -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a current string value.<hr>

**[Returns]**

- `value`: str
  - Current string value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> string: ap.String = ap.String('Hello')
>>> string.value = 'World!'
>>> string.value
'World!'
```

<hr>

**[References]**

- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)