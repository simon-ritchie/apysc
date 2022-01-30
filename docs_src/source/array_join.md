# Array class join interface

This page explains the `Array` class `join` method interface.

## What interface is this?

The `join` method returns a joined `String` with the specified separator string.

## Basic usage

The `join` method requires the `sep` argument as the separator, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2, 3])
joined: ap.String = arr.join(sep=',')
assert joined == '1,2,3'
```


## join API

<!-- Docstring: apysc._type.array.Array.join -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `join(self, sep:Union[str, apysc._type.string.String]) -> apysc._type.string.String`<hr>

**[Interface summary]** Join this array value with a specified separator string.<hr>

**[Parameters]**

- `sep`: String or str
  - Separator string.

<hr>

**[Returns]**

- `joined`: String
  - Joined string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.join(sep=', ')
String('1, 2, 3')
```