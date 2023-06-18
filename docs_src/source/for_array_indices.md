# ForArrayIndices class

This page explains the `ForArrayIndices` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What class is this?

The `ForArrayIndices` class is the for-loop class.

This interface returns `Array`'s index (starts with 0) in a loop.

## Basic usage

This class requires using the `with`-statement.

The `as`-keyword value becomes the `Int` type index.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

arr: ap.Array[ap.Number] = ap.Array([ap.Number(50), ap.Number(150), ap.Number(250)])
indices: ap.Array[ap.Int] = ap.Array([])
with ap.ForArrayIndices(arr=arr) as i:
    indices.append(i)

ap.assert_arrays_equal(indices, [0, 1, 2])

ap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_1/")
```

<iframe src="static/for_array_indices_basic_usage_1/index.html" width="0" height="0"></iframe>

The following example uses an index and sets a circle center-x coordinate.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color="#333", stage_elem_id="stage"
)

x_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])
with ap.ForArrayIndices(arr=x_arr) as i:
    x: ap.Number = x_arr[i]
    circle: ap.Circle = ap.Circle(
        x=x,
        y=75,
        radius=25,
        fill_color="#0af",
    )

ap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_2/")
```

<iframe src="static/for_array_indices_basic_usage_2/index.html" width="350" height="150"></iframe>

## See also

- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
  - Notes: This class also has the same arguments and behaves in the same way.

## ForArrayIndices API

<!-- Docstring: apysc._loop.for_array_indices.ForArrayIndices.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, arr: apysc._type.array.Array, *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The loop implementation class for the `ap.Array` indices.<hr>

**[Parameters]**

- `arr`: Array
  - An array to iterate.
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
>>> arr: ap.Array[ap.Number] = ap.Array(
...     [ap.Number(50), ap.Number(150), ap.Number(250)]
... )
>>> indices: ap.Array[ap.Int] = ap.Array([])
>>> with ap.ForArrayIndices(arr=arr) as i:
...     indices.append(i)
...
>>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])
```

<hr>

**[References]**

- [Why the apysc library doesn’t use the Python built-in data type](https://simon-ritchie.github.io/apysc/en/why_apysc_doesnt_use_python_builtin_data_type.html)
- [Each branch instruction class’s scope variable reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)