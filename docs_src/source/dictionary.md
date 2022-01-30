# Dictionary

This page explains the `Dictionary` class.

Before reading on, maybe it is helpful to read the following page:

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Dictionary?

The `Dictionary` class is the apysc dictionary class. It behaves like the Python built-in `dict` value.

## Constructor method

The `Dictionary` class constructor method requires a Python built-in `dict` or `Dictionary` value:

```py
# runnable
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
assert dict_1 == {'a': 10}

dict_2: ap.Dictionary = ap.Dictionary(dict_1)
assert dict_1 == dict_2
```

## Value setter interface

A `Dictionary` value can be updated by indexing, like the Python built-in `dict` value:

```py
# runnable
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({'a': 10})
dict_1['a'] = 20
assert dict_1 == {'a': 20}
```

## Value getter interface

A `Dictionary` value also can be retrieved by indexing:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
dict_1: ap.Dictionary = ap.Dictionary({'a': int_1})
int_2: ap.Int = dict_1['a']
assert isinstance(int_2, ap.Int)
assert int_2 == 10
```

## Notes of the getter interface

If a `Dictionary` value doesn't have the specified key, a retrieved value type becomes the `AnyValue` type. This behavior occasionally is helpful when a `Dictionary` value is updated dynamically (e.g., updating by the JavaScript event handler).

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
dict_1: ap.Dictionary = ap.Dictionary({'a': int_1})
retrieved_val: ap.AnyValue = dict_1['b']
assert isinstance(retrieved_val, ap.AnyValue)
```

## Value deletion interface

A `Dictionary` value can be deleted by the `del` statement, as follows:

```py
# runnable
import apysc as ap

int_1: ap.Int = ap.Int(10)
dict_1: ap.Dictionary = ap.Dictionary({'a': int_1})
del dict_1['a']
assert dict_1 == {}
```


## Dictionary class constructor API

<!-- Docstring: apysc._type.dictionary.Dictionary.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, value:Union[Dict[~_K, ~_V], _ForwardRef('Dictionary')]) -> None`<hr>

**[Interface summary]** Dictionary class for the apysc library.<hr>

**[Parameters]**

- `value`: dict or Dictionary
  - Initial dictionary value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({'a': 10})
>>> dictionary
Dictionary({'a': 10})

>>> dictionary['a']
10

>>> dictionary['b'] = 20
>>> dictionary['b']
20
```

<hr>

**[References]**

- [Dictionary class generic type settings document](https://simon-ritchie.github.io/apysc/dictionary_generic.html)

## value attribute API

<!-- Docstring: apysc._type.dictionary.Dictionary.value -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get a current dict value.<hr>

**[Returns]**

- `value`: dict
  - Current dict value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({})
>>> dictionary.value = {'a': 10}
>>> dictionary.value
{'a': 10}
```

<hr>

**[References]**

- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/fundamental_data_classes_value_interface.html)