# Boolean class

This page explains the `Boolean` class.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Boolean class?

The `Boolean` class is the apysc boolean class. It can accept `bool` or `Boolean` values at the constructor, as follows:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1

bool_2: ap.Boolean = ap.Boolean(False)
assert not bool_2

bool_3: ap.Boolean = ap.Boolean(bool_1)
assert bool_3
```

## Note for the Bool class alias

The `Bool` class is the alias of the `Boolean` class. And it behaves the same as the `Boolean` class.

```py
# runnable
import apysc as ap

_ = ap.Stage()
assert ap.Boolean == ap.Bool
assert ap.Boolean(True) == ap.Bool(True)
```

## Boolean comparison

The `Boolean` comparison interface behaves like the Python built-in `bool` value.

You can compare it with the equal comparison operator (`==`), and the `Boolean`\, `bool`\, `int`\, `Int` types are acceptable, as follows:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1 == True  # noqa
assert bool_1 == ap.Boolean(True)
assert bool_1 == 1
assert bool_1 == ap.Int(1)
```

Also, the not equal comparison operator (`!=`) is supported, as follows:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1 != False  # noqa
assert bool_1 != ap.Boolean(False)
assert bool_1 != 0
assert bool_1 != ap.Int(0)
```

You can skip the comparison operator, as follows:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
assert bool_1

bool_2: ap.Boolean = ap.Boolean(False)
assert not bool_2
```

## Reverse a Boolean value

The `not_` property returns the reversed `Boolean` value:

```py
# runnable
import apysc as ap

_ = ap.Stage()
bool_1: ap.Boolean = ap.Boolean(True)
bool_2: ap.Boolean = bool_1.not_
assert not bool_2

bool_3: ap.Boolean = bool_2.not_
assert bool_3
```


## Boolean class constructor API

<!-- Docstring: apysc._type.boolean.Boolean.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value: Union[bool, typing_extensions.Literal[0, 1], apysc._type.int.Int, ForwardRef('Boolean')], *, variable_name_suffix: str = '', skip_init_substitution_expression_appending: bool = False) -> None`<hr>

**[Interface summary]**

Boolean class for apysc library.<hr>

**[Parameters]**

- `value`: Boolean or Int or bool or int
  - Initial boolean value. 0 or 1 are acceptable for an integer value.
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.
- `skip_init_substitution_expression_appending`: bool, default False
  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.

<hr>

**[Notes]**

The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> bool_val_1: ap.Boolean = ap.Boolean(True)
>>> bool_val_1
Boolean(True)

>>> bool_val_2: ap.Bool = ap.Bool(True)
>>> bool_val_2
Boolean(True)
```

<hr>

**[References]**

- [True_ and False_ constants](https://simon-ritchie.github.io/apysc/en/true_and_false.html)

## value property API

<!-- Docstring: apysc._type.boolean.Boolean.value -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a current boolean value.<hr>

**[Returns]**

- `value`: bool
  - Current boolean value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> bool_val: ap.Boolean = ap.Boolean(True)
>>> bool_val.value = False
>>> bool_val.value
False

>>> bool_val.value = ap.Boolean(True)
>>> bool_val.value
True
```

<hr>

**[References]**

- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)

## not_ property API

<!-- Docstring: apysc._type.boolean.Boolean.not_ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a not condition Boolean value.<hr>

**[Returns]**

- `result`: Boolean
  - Not condition Boolean value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> bool_val: ap.Boolean = ap.Boolean(True)
>>> bool_val.not_
Boolean(False)

>>> bool_val.value = False
>>> bool_val.not_
Boolean(True)
```