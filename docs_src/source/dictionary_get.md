# Dictionary get interface

This page explains the `Dictionary` class `get` method interface.

## What interface is this?

The `get` method returns the specified key's value. If that key does not exist in the dictionary, it returns the default value (not raising an exception).

## Basic usage

The `get` method requires the first argument, `key` (dictionary key). The second argument of the `default` is optional, and if not provided, it returns the `None` value.

```py
# runnable
from typing import Any, Optional

import apysc as ap

dict_val: ap.Dictionary = ap.Dictionary({'a': 10})
got_val_1: int = dict_val.get(key='a', default=0)
assert got_val_1 == 10

got_val_2: int = dict_val.get(key='b', default=0)
assert got_val_2 == 0

got_val_3: Optional[Any] = dict_val.get(key='b')
assert got_val_3 is None
```