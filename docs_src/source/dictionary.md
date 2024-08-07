# Dictionary

This page will explain the `Dictionary` class.

Before reading on, maybe it is useful to read the following page:

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

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

If a `Dictionary` value doesn't have the specified key, then a retrieved value type will be the `AnyValue` type. This behavior will occasionally be useful when a `Dictionary` value is updated dynamically (e.g., updating by the JavaScript event handler).

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
