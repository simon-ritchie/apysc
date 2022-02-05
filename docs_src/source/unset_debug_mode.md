# unset_debug_mode interface

This page explains the `unset_debug_mode` function interface.

## What interface is this?

The `unset_debug_mode` function interface unsets the debug mode setting. It stops the debug information appending.

The debug mode exports lots of information. Sometimes it becomes cumbersome. In that case, stopping the debug mode is helpful when it is no longer needed.

## Notes

If the exporting interface (e.g., `ap.save_overall_html`) `minify` option is enabled, it removes debug mode information. So it is required to set the `minify=False` when you use the `unset_debug_mode` interface.

## Basic usage

The `unset_debug_mode` interface requires no arguments.

The following example appends the debug information only at the `int_1` instantiation and incremental addition of 10.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
ap.set_debug_mode()
int_1: ap.Int = ap.Int(10)
int_1 += 10
ap.unset_debug_mode()
int_2: ap.Int = ap.Int(20)
int_2 += 20

ap.save_overall_html(
    minify=False, dest_dir_path='unset_debug_mode_basic_usage/')
```

The exported HTML includes the debug information at the first integer position. It doesn't include the sprite and second integer positions, as follows:

```js
...
  var sp_1 = stage.nested();
  var g_1 = stage.nested();
  arr_2.push(g_1);
  var i_12 = -1;
  i_12 = arr_2.indexOf(g_1);
  var b_3 = false;
  var i_13 = -1;
...
  //////////////////////////////////////////////////////////////////////
  // [__init__ 12] started.
  // module name: apysc._type.int
  // class: Int
  // arguments and variables:
  //    value = 10
  //    self = 0()
    //////////////////////////////////////////////////////////////////////
    // [__init__ 14] started.
    // module name: apysc._type.number_value_interface
    // class: NumberValueInterface
    // arguments and variables:
    //    type_name = 'i'
    //    value = 10
    //    self = 0(i_16)
    // [__init__ 14] ended.
    // module name: apysc._type.number_value_interface
    // class: NumberValueInterface
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [to_int_from_float 14] started.
    // module name: apysc._converter.cast
    // arguments and variables:
    //    int_or_float = 10
    // [to_int_from_float 14] ended.
    // module name: apysc._converter.cast
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [append_constructor_expression 14] started.
    // module name: apysc._type.number_value_interface
    // class: NumberValueInterface
    // arguments and variables:
    //    self = 10(i_16)
      var i_16 = 10;
    // [append_constructor_expression 14] ended.
    // module name: apysc._type.number_value_interface
    // class: NumberValueInterface
    //////////////////////////////////////////////////////////////////////
...
  var i_18 = 20;
  var i_19 = cpy(i_18);
  var i_19 = i_18 + 20;
  i_18 = i_19;
...
```

## See also

- [Set debug mode interface](set_debug_mode.md)
- [DebugInfo class](debug_info.md)


## unset_debug_mode API

<!-- Docstring: apysc._html.debug_mode.unset_debug_mode -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unset_debug_mode() -> None`<hr>

**[Interface summary]** Unset the debug mode for the HTML and JavaScript debugging.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
>>> ap.unset_debug_mode()
```