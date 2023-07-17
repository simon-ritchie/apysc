# String class

This page explains the `String` class.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the String class?

The `String` class is the apysc string class. It can accept `str` or `String` values at the constructor, as follows:

```py
# runnable
import apysc as ap

ap.Stage()
string_1: ap.String = ap.String("Hello")
assert string_1 == "Hello"

string_2: ap.String = ap.String(string_1)
assert string_2 == "Hello"
```

## String class interfaces

For more details about the `String` class each interface, please see the following:

- [String class comparison operations](string_comparison_operations.md)
- [String class addition and multiplication operations](string_addition_and_multiplication.md)


## String class constructor API

<!-- Docstring: apysc._type.string.String.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value: Union[str, ForwardRef('String')], *, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[Interface summary]**

String class for apysc library.<hr>

**[Parameters]**

- `value`: String or str
  - Initial string value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.

<hr>

**[Notes]**

The `Str` class is the alias of `String`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string: ap.String = ap.String("Hello")
>>> string
String("Hello")

>>> string += " World!"
>>> string
String("Hello World!")
```

<hr>

**[References]**

- [String class comparison operations](https://simon-ritchie.github.io/apysc/en/string_comparison_operations.html)
- [String class addition and multiplication operations](https://simon-ritchie.github.io/apysc/en/string_addition_and_multiplication.html)

## value property API

<!-- Docstring: apysc._type.string.String.value -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current string value.<hr>

**[Returns]**

- `value`: str
  - Current string value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> string: ap.String = ap.String("Hello")
>>> string.value = "World!"
>>> string.value
'World!'
```

<hr>

**[References]**

- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)