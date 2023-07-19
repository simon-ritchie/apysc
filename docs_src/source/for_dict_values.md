# ForDictValues class

This page explains the `ForDictValues` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What class is this?

The `ForDictValues` class is the for-loop class.

This interface returns `Dictionary`'s value in a loop.

## Basic usage

This class requires using the `with`-statement.

The `as`-keyword value becomes a `Dictionary`'s value.

Also, this class requires the `dict_value_type` argument to specify a type of `Dictionary`'s value type.

This type only accepts an apysc type, such as the `String`, `Int`, or `Rectangle`.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color="#333", stage_elem_id="stage"
)
dict_: ap.Dictionary[str, ap.Number] = ap.Dictionary(
    {"a": ap.Number(50), "b": ap.Number(150)},
)
with ap.ForDictValues(dict_=dict_, dict_value_type=ap.Number) as value:
    ap.Rectangle(x=value, y=50, width=50, height=50, fill_color="#0af")

ap.save_overall_html(dest_dir_path="for_dict_values_basic_usage_1/")
```

<iframe src="static/for_dict_values_basic_usage_1/index.html" width="250" height="150"></iframe>

## See also

- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
  - Notes: This class also has the same arguments and behaves in the same way.

## ForDictValues API

<!-- Docstring: apysc._loop.for_dict_values.ForDictValues.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, dict_: apysc._type.dictionary.Dictionary[typing.Any, ~_DictValue], dict_value_type: Type[~_DictValue], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The loop implementation class for the `ap.Dictionary` values.<hr>

**[Parameters]**

- `dict_`: Dictionary[Any, _DictValue]
  - A dictionary to iterate.
- `dict_value_type`: Type[_DictValue]
  - A dictionary value type. This interface accepts `InitializeWithBaseValueInterface` subclasses, such as the `Int`, `String`, or `Rectangle`.
- `locals_`: Optional[Dict[str, Any]], optional
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a with-statement scope. This setting is useful when you don't want to update each variable.
- `globals_`: Optional[Dict[str, Any]], optional
  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.