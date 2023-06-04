# For class

This page explains the `For` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses the `For` class for the same reason for each data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the For class?

The `For` class is the apysc for loop class. It behaves like the Python built-in `for` keyword.

## Basic usage

The `For` class requires using the `with` statement. The `as` keyword value becomes the `Int` type index (an `i` variable)  or `String` type key.

The following example draws the three rectangles in the `with For` block:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color="#0af")

arr: ap.Array[int] = ap.Array(range(3))
i: ap.Int
with ap.For(arr) as i:
    sprite.graphics.draw_rect(x=i * 100 + 50, y=50, width=50, height=50)

ap.save_overall_html(dest_dir_path="for_basic_usage/")
```

<iframe src="static/for_basic_usage/index.html" width="350" height="150"></iframe>

The `For` class constructor's first argument accepts an `Array` or `Dictionary` value. If you pass a `Dictionary` value, the `as` keyword value becomes a `String` value, not `Int`\.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()

dict_val: ap.Dictionary = ap.Dictionary(
    {"magenta": ap.String("#f0a"), "cyan": ap.String("#0af")}
)
key: ap.String
with ap.For(dict_val) as key:
    color: ap.String = dict_val[key]
    sprite.graphics.begin_fill(color=color)
    condition_1: ap.Boolean = key == "magenta"
    condition_2: ap.Boolean = key == "cyan"
    with ap.If(condition_1):
        sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    with ap.Elif(condition_2):
        sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

ap.save_overall_html(dest_dir_path="for_basic_usage_with_dict/")
```

<iframe src="static/for_basic_usage_with_dict/index.html" width="250" height="150"></iframe>

## See also

- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
  - Notes: the `For` class also has the same arguments and behaves in the same way.


## For API

<!-- Docstring: apysc._loop._for.For.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, arr_or_dict: Union[apysc._type.array.Array, apysc._type.dictionary.Dictionary], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None) -> None`<hr>

**[Interface summary]**

The class to append for the (loop) expression.<hr>

**[Parameters]**

- `arr_or_dict`: Array or Dictionary
  - Array or Dictionary instance to iterate.
- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a `For` scope. This setting is useful when you don't want to update each variable by implementing the `For` scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> arr: ap.Array = ap.Array(range(3))
>>> with ap.For(arr) as i:
...     ap.trace("Loop index is:", i)
...
```