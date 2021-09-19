# set_debug_mode interface

This page will explain the `set_debug_mode` function interface.

## What interface is this?

The `set_debug_mode` function interface will set the debug mode setting and the debug information (Python function or method calls and arguments information) will be appended to the exported HTML.

## Notes

The debug mode setting will append lots of information to the HTML, so the exporting time will be longer and the HTML file will be bigger.

Also, the `minify` setting will be ignored.

## Basic usage

You can set the debug mode by the `set_debug_mode` after the stage instantiation. This function requires the stage instance since the stage instance will reset the settings at first, including the debug mode.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
ap.set_debug_mode(stage=stage)
sprite: ap.Sprite = ap.Sprite(stage=stage)
int_1: ap.Int = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='set_debug_mode_basic_usage/')
```

The exported HTML will be appended the information (Python's function and method callings, its module and class names, and argument information) as the JavaScript comment, like the following:

```js
...
  //////////////////////////////////////////////////////////////////////
  // [__init__ 1] started.
  // module name: apysc._display.sprite
  // class: Sprite
  // arguments and variables:
  //    variable_name = None
  //    stage = Stage('stage')(stage)
  //    self = Sprite('')()
    //////////////////////////////////////////////////////////////////////
    // [__init__ 2] started.
    // module name: apysc._type.array
    // class: Array
    // arguments and variables:
    //    value = []
    //    self = []()
      //////////////////////////////////////////////////////////////////////
      // [_append_constructor_expression 2] started.
      // module name: apysc._type.array
      // class: Array
      // arguments and variables:
      //    self = [](arr_2)
        var arr_2 = [];
      // [_append_constructor_expression 2] ended.
      // module name: apysc._type.array
      // class: Array
      //////////////////////////////////////////////////////////////////////
    // [__init__ 2] ended.
    // module name: apysc._type.array
    // class: Array
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [__init__ 1] started.
    // module name: apysc._display.display_object
    // class: DisplayObject
    // arguments and variables:
    //    variable_name = 'sp_1'
    //    stage = Stage('stage')(stage)
    //    self = Sprite('')()
    // [__init__ 1] ended.
    // module name: apysc._display.display_object
    // class: DisplayObject
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    // [_append_constructor_expression 1] started.
    // module name: apysc._display.sprite
    // class: Sprite
    // arguments and variables:
    //    self = Sprite('sp_1')(sp_1)
      var sp_1 = stage.nested();
    // [_append_constructor_expression 1] ended.
    // module name: apysc._display.sprite
    // class: Sprite
    //////////////////////////////////////////////////////////////////////
...
```

## See also

- [Unset debug mode interface](unset_debug_mode.md)
- [DebugInfo class](debug_info.md)
