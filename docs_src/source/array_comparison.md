# Array class comparison interfaces

This page will explain the `Array` class comparison interfaces (equal and not equal comparison).

## Basic usage

The `Array` value can compare with a Python built-in `list` value and `Array` value. A return value will be the `Boolean` type.

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
result: ap.Boolean = arr == [1, 3, 5]
assert result
```

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
other_arr: ap.Array[int] = ap.Array([1, 3, 5])
result: ap.Boolean = arr == other_arr
assert result
```

The equal comparison operator (`==`) and not equal comparison operator (`!=`) are supported:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 3, 5])
result: ap.Boolean = arr != [2, 4, 6]
assert result
```
