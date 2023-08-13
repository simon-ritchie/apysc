# set_debug_mode interface

This page explains the `set_debug_mode` function interface.

## What interface is this?

The `set_debug_mode` function interface sets the debug mode setting. This setting appends the debug information (Python function or method calls and arguments information) to the exported HTML.

## Notes

The debug mode setting appends lots of information to the HTML. As a result, the exporting time becomes long, and the HTML file size becomes large.

Also, this setting ignores the `minify` setting.

## Basic usage

After the stage instantiation, you can set the debug mode by the `set_debug_mode` function.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
ap.set_debug_mode()
sprite: ap.Sprite = ap.Sprite()
int_1: ap.Int = ap.Int(10)

ap.save_overall_html(dest_dir_path="set_debug_mode_basic_usage/")
```

This setting appends the information (Python's function and method callings, its module and class names, and argument information) as the JavaScript comment to the exported HTML, like the following:

```js
...
  //////////////////////////////////////////////////////////////////////
  // [__init__ 1] started.
  // module name: apysc._display.sprite
  // class: Sprite
  // arguments and variables:
  //    variable_name = None
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

- [unset_debug_mode interface](unset_debug_mode.md)


## set_debug_mode API

<!-- Docstring: apysc._html.debug_mode.set_debug_mode -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `set_debug_mode() -> None`<hr>

**[Interface summary]**

Set the debug mode for the HTML and JavaScript debugging. If calling this function, this interface applies the following setting: <br> ・Disabling HTML minify setting. <br> ・Changing to append per each interface JavaScript divider string.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
```