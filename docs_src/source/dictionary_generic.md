# Dictionary class generic type settings

This page explains the `Dictionary` class key and value's generic type settings.

## Basic usage

You can specify the key and value's type at the `Dictionary` type-annotation, as follows:

```py
# runnable
import apysc as ap

dict_value: ap.Dictionary[str, int] = ap.Dictionary({'a': 10})
a_value: int = dict_value['a']
```

These generic type-annotations are sometimes helpful for checking with the mypy, Pylance, or other libraries and enhancing safety.

For example, the following code raises an error of value's type when checking with the Pylance:

```py
# runnable
import apysc as ap

dict_value: ap.Dictionary[str, int] = ap.Dictionary({'a': 10})
a_value: str = dict_value['a']
```

```
Expression of type "int" cannot be assigned to declared type "str"
  "int" is incompatible with "str"
```

Also, the following code raises an error of key's type (`str` is required but `int` is specified):

```py
# runnable
import apysc as ap

dict_value: ap.Dictionary[str, int] = ap.Dictionary({'a': 10})
a_value: int = dict_value[10]
```

If you need to use multiple types and type checking, then use the `Union`\, as follows:

Notes: Alternatively, use the `|` symbol, if you are using Python 3.10 or later) or `Any` type.

```py
# runnable
from typing import Union

import apysc as ap

# Accepting the str and int key types.
dict_value: ap.Dictionary[Union[int, str], int] = ap.Dictionary(
    {'a': 10, 2: 20})
a_value: int = dict_value['a']
b_value: int = dict_value[2]
```

```py
# runnable
from typing import Any

import apysc as ap

# Accepting all types by specifying the Any type.
dict_value: ap.Dictionary[Any, Any] = ap.Dictionary(
    {'a': 10, 2: 'b'})
a_value: int = dict_value['a']
b_value: str = dict_value[2]
```
