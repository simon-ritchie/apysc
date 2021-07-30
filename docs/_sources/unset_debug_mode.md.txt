# unset_debug_mode interface

This page will explain the `unset_debug_mode` function interface.

## What interface is this?

The `unset_debug_mode` function interface will unset the debug mode setting and the debug information appending will be stopped.

The debug mode will export lots of information and sometimes it will be cumbersome and in that case, stop the debug mode at the point where it is no longer needed.

## Notes

If the exporting interface (e.g., `ap.save_overall_html`) `minify` option is enabled, debug mode information will be removed. So it is required to set the `minify=False` when you use the `unset_debug_mode` interface.

## Basic usage

The `unset_debug_mode` interface requires no arguments.

The following example will append the debug information only at the `int_1` instantiation and incremental addition of 10.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
ap.set_debug_mode(stage=stage)
int_1: ap.Int = ap.Int(10)
int_1 += 10
ap.unset_debug_mode()
int_2: ap.Int = ap.Int(20)
int_2 += 20

ap.save_overall_html(
    minify=False, dest_dir_path='unset_debug_mode_basic_usage/')
```

## See also

- [Set debug mode interface](set_debug_mode.md)
