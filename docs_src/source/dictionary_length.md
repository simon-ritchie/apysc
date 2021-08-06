# Dictionary length interface

This page will explain the `Dictionary` class `length` property interface.

## What interface is this?

The `length` property will return the length of dictionary keys.

## Basic usage

The `length` property interface returns the `Int` value. There is no setter interface.

```py
# runnable
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
assert dict_1.length == 2
assert isinstance(dict_1.length, ap.Int)
```

## Note for the len function

The Python built-in `len` function is not supported and raises an exception:

```py
import apysc as ap

dict_1: ap.Dictionary = ap.Dictionary({'a': 10, 'b': 20})
len(dict_1)
```

```
Exception: Dictionary instance can't apply len function. Please use length property instead.
```
