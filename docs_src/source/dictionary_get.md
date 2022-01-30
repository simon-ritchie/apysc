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

## get API

<!-- Docstring: apysc._type.dictionary.Dictionary.get -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get(self, key:Union[~_K, apysc._type.expression_string.ExpressionString], *, default:~DefaultType=None) -> ~DefaultType`<hr>

**[Interface summary]** Get a specified key dictionary value. If this dictionary hasn't a specified key, this interface returns a default value.<hr>

**[Parameters]**

- `key`: _K
  - Target key.
- `default`: DefaultType or None, optional
  - Any default value.

<hr>

**[Returns]**

- `result_value`: Any
  - Extracted value or a default value.

<hr>

**[Examples]**

```py
>>> from typing import Optional
>>> import apysc as ap
>>> dictionary: ap.Dictionary = ap.Dictionary({'a': 10})
>>> value_1: Optional[int] = dictionary.get('a')
>>> value_1
10

>>> value_2: Optional[int] = dictionary.get('b')
>>> print(value_2)
None

>>> value_3: int = dictionary.get('c', default=0)
>>> value_3
0
```