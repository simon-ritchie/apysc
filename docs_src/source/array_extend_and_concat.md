# Array class extend and concat interfaces

This page explains the `Array` class `extend` and `concat` method interfaces.

## What interfaces are these?

The `extend` and `concat` method interfaces are the two arrays' concatenation interfaces.

The `extend` method updates an original array in place and returns the `None`. The `concat` method returns the concatenated array, and an original one is not updated.

## Basic usage

The `extend` and `concat` methods require other iterable objects, like the `list`\, `tuple`\, or `Array` value at the first argument, as follows:

```py
# runnable
import apysc as ap

arr: ap.Array[int] = ap.Array([1, 2])
arr.extend([3, 4])
assert arr == [1, 2, 3, 4]

other_arr: ap.Array[int] = arr.concat([5, 6])
assert other_arr == [1, 2, 3, 4, 5, 6]
assert arr == [1, 2, 3, 4]
```


## extend API

<!-- Docstring: apysc._type.array.Array.extend -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `extend(self, other_arr:Union[List[~T], tuple, _ForwardRef('Array')]) -> None`<hr>

**[Interface summary]** Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to the concat method. Still, there is a difference in whether updating the same variable (extend) or returned as a different variable (concat).<hr>

**[Parameters]**

- `other_arr`: list or tuple or Array
  - Other array-like values to concatenate.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr.extend([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```

## concat API

<!-- Docstring: apysc._type.array.Array.concat -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `concat(self, other_arr:Union[List[~T], tuple, _ForwardRef('Array')]) -> 'Array'`<hr>

**[Interface summary]** Concatenate argument array to this one. This interface positions the argument array's values after this array values. This method is similar to extend method, but there is a difference in whether updating the same variable (extend) or returned as a different variable (concat).<hr>

**[Parameters]**

- `other_arr`: list or tuple or Array
  - Other array-like values to concatenate.

<hr>

**[Returns]**

- `concatenated`: Array
  - Concatenated array value.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array([1, 2, 3])
>>> arr = arr.concat([4, 5, 6])
>>> arr
Array([1, 2, 3, 4, 5, 6])
```