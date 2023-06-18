# ForDictKeys class

This page explains the `ForDictKeys` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What class is this?

The `ForDictKeys` class is the for-loop class.

This interface returns `Dictionary`'s key in a loop.

## Basic usage

This class requires using the `with`-statement.

The `as`-keyword value becomes a `Dictionary`'s key.

Also, this class requires the `dict_key_type` to specify a type of `Dictionary`'s key type.

This type only accepts an apysc type, such as the `String`, `Int`, or `Boolean`.

```py
# runnable
import apysc as ap

ap.Stage(stage_width=0, stage_height=0, background_color="#333", stage_elem_id="stage")

dict_: ap.Dictionary[ap.String, int] = ap.Dictionary(
    {
        ap.String("apple"): 120,
        ap.String("orange"): 200,
    }
)
keys: ap.Array[ap.String] = ap.Array([])
with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
    keys.append(key)
ap.assert_arrays_equal(
    keys,
    ["apple", "orange"],
)

ap.save_overall_html(dest_dir_path="for_dict_keys_basic_usage_1/")
```

<iframe src="static/for_dict_keys_basic_usage_1/index.html" width="0" height="0"></iframe>

## See also

- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
  - Notes: This class also has the same arguments and behaves in the same way.

## ForDictKeys API

<!-- Docstring: apysc._loop.for_dict_keys.ForDictKeys.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, dict_: apysc._type.dictionary.Dictionary[~_DictKey, typing.Any], dict_key_type: Type[~_DictKey], *, locals_: Union[Dict[str, Any], NoneType] = None, globals_: Union[Dict[str, Any], NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The loop implementation class for the `ap.Dictionary` keys.<hr>

**[Parameters]**

- `dict_`: Dictionary[_DictKey, Any]
  - A dictionary to iterate.
- `dict_key_type`: Type[_DictKey]
  - A dictionary key type. This interface accepts hashable types, such as the `String`, `Int`, or `Boolean`.
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
>>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(
...     {
...         ap.String("apple"): ap.Boolean(True),
...         ap.String("orange"): ap.Boolean(False),
...     }
... )
>>> keys: ap.Array[ap.String] = ap.Array([])
>>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
...     keys.append(key)
...
>>> ap.assert_arrays_equal(
...     keys,
...     ["apple", "orange"],
... )
```