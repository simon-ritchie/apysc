# ForArrayIndicesAndValues class

This page explains the `ForArrayIndicesAndValues` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What class is this?

The `ForArrayIndicesAndValues` class is the for-loop class.

This interface returns `Array`'s index and value in a loop.

## Basic usage

This class requires using the `with`-statement.

The `as`-keyword value becomes an `Array`'s index and value.

Also, this class requires the `arr_value_type` to specify a type of an `Array`'s value type.

This type only accepts an apysc type, such as the `Int`, `Number`, `String`, or `Rectangle`.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350,
    stage_height=225,
    background_color=ap.Color("#333"),
)

x_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])
with ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (i, x):
    circle: ap.Circle = ap.Circle(
        x=x,
        y=(i + 1) * 50,
        radius=25,
        fill_color=ap.Color("#0af"),
    )

ap.save_overall_html(dest_dir_path="for_array_indices_and_values_basic_usage_1/")
```

<iframe src="static/for_array_indices_and_values_basic_usage_1/index.html" width="350" height="225"></iframe>

## See also

- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
  - Notes: This class also has the same arguments and behaves in the same way.

## ForArrayIndicesAndValues API

<!-- Docstring: apysc._loop.for_array_indices_and_values.ForArrayIndicesAndValues.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, arr: apysc._type.array.Array[~_ArrayValue], arr_value_type: Type[~_ArrayValue], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The loop implementation class for the `ap.Array` indices and values.<hr>

**[Parameters]**

- `arr`: Array[_ArrayValue]
  - An array to iterate.
- `arr_value_type`: Type[_ArrayValue]
  - An array value type. This interface accepts apysc types, such as the `Int`, `String`, `Rectangle`.
- `locals_`: Optional[Dict[str, Any]], optional
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a with-statement scope. This setting is useful when you don't want to update each variable.
- `globals_`: Optional[Dict[str, Any]], optional
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     stage_width=350, stage_height=225, background_color=ap.Color("#333")
... )
>>> x_arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(75), ap.Number(175), ap.Number(275)]
... )
>>> with ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (
...     i,
...     x,
... ):
...     circle: ap.Circle = ap.Circle(
...         x=x,
...         y=(i + 1) * 50,
...         radius=25,
...         fill_color=ap.Color("#0af"),
...     )
```