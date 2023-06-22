# ForDictKeysAndValues class

This page explains the `ForDictKeysAndValues` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What class is this?

The `ForDictKeysAndValues` class is the for-loop class.

This interface returns `Dictionary`'s key and value in a loop.

## Basic usage

This class requires using the `with`-statement.

The `as`-keyword value becomes a `Dictionary`'s key and value.

Also, this class requires the `dict_key_type` and `dict_value_type` arguments to specify types of `Dictionary`'s key and value types.

The `dict_key_type` only accepts a hashable apysc type, such as the `String`, `Int`, `Number`, and `Boolean`.

Similarly, the `dict_value_type` only accepts an apysc type, such as the `String`, `Int`, or `Rectangle`.

```py
# runnable
import apysc as ap

ap.Stage(background_color="#333", stage_width=250, stage_height=300)

dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(
    {
        ap.Number(50): ap.Number(50),
        ap.Number(100): ap.Number(125),
        ap.Number(150): ap.Number(200),
    }
)
with ap.ForDictKeysAndValues(
    dict_=dict_,
    dict_key_type=ap.Number,
    dict_value_type=ap.Number,
) as (key, value):
    ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")

ap.save_overall_html(dest_dir_path="for_dict_keys_and_values_basic_usage_1/")
```

<iframe src="static/for_dict_keys_and_values_basic_usage_1/index.html" width="250" height="300"></iframe>

## See also

- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
  - Notes: This class also has the same arguments and behaves in the same way.

## ForDictKeysAndValues API

<!-- Docstring: apysc._loop.for_dict_keys_and_values.ForDictKeysAndValues.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, dict_: apysc._type.dictionary.Dictionary[~_DictKey, ~_DictValue], dict_key_type: Type[~_DictKey], dict_value_type: Type[~_DictValue], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The loop implementation class for the `ap.Dictionary` keys and values.<hr>

**[Parameters]**

- `dict_`: Dictionary[_DictKey, _DictValue]
  - A dictionary to iterate.
- `dict_key_type`: Type[_DictKey]
  - A dictionary key type. This interface accepts hashable types, such as the `String`, `Int`, `Number`, or `Boolean`.
- `dict_value_type`: Type[_DictValue]
  - A dictionary value type. This interface accepts `InitializeForLoopKeyOrValueInterface` subclasses, such as the `Int`, `String`, or `Rectangle`.
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
>>> _ = ap.Stage(background_color="#333", stage_width=250, stage_height=300)
>>> dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(
...     {
...         ap.Number(50): ap.Number(50),
...         ap.Number(100): ap.Number(125),
...         ap.Number(150): ap.Number(200),
...     }
... )
>>> with ap.ForDictKeysAndValues(
...     dict_=dict_,
...     dict_key_type=ap.Number,
...     dict_value_type=ap.Number,
... ) as (key, value):
>>>     _ = ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")
```