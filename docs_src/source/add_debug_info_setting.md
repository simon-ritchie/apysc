# add_debug_info_setting decorator interface

## What interface is this?

The `add_debug_info_setting` decorator interface sets the debug information settings to a target function or method.

A decorated function or method exports debug information when you enable the debug mode setting.

## Basic usage

It is necessary to set the debug mode setting with the `ap.set_debug_mode()` function at the first position.

After that, You can set the `@ap.add_debug_info_setting` decorator settings to any function or method.

The `@ap.add_debug_info_setting` needs to specify the `module_name` (this value becomes `__name__`).

```py
# runnable
import apysc as ap


def _main() -> None:
    """The entry point of this project."""
    ap.Stage(
        background_color="#333",
        stage_width=150,
        stage_height=150,
        stage_elem_id="stage",
    )
    ap.set_debug_mode()
    _draw_rectangle(x=50, y=50)
    ap.save_overall_html(dest_dir_path="add_debug_info_setting_basic_usage/")


@ap.add_debug_info_setting(module_name=__name__)
def _draw_rectangle(*, x: int, y: int) -> None:
    """
    Draw a rectangle with the given coordinates and sprite
    container class.

    Parameters
    ----------
    x : int
        X-coordinate of the rectangle.
    y : int
        Y-coordinate of the rectangle.
    """
    _: MySprite = MySprite(x=x, y=y)


class MySprite(ap.Sprite):
    @ap.add_debug_info_setting(module_name=__name__)
    def __init__(self, *, x: int, y: int) -> None:
        """
        My rectangle's sprite container class.

        Parameters
        ----------
        x : int
            X-coordinate of the rectangle.
        y : int
            Y-coordinate of the rectangle.
        """
        super(MySprite, self).__init__()
        self.graphics.begin_fill(color="#0af")
        self.graphics.draw_rect(x=x, y=y, width=50, height=50)


if __name__ == "__main__":
    _main()
```

The exported HTML contains the following debug information (function and method calling information):

```
...
  //////////////////////////////////////////////////////////////////////
  // [_draw_rectangle 1] started.
  // module name: __main__
  // Keyword arguments: {'x': 50, 'y': 50}
    //////////////////////////////////////////////////////////////////////
    // [__init__ 1] started.
    // module name: __main__
    // class: MySprite
    // Positional arguments: [Sprite('')]
    // Keyword arguments: {'x': 50, 'y': 50}
...
```

## Notes of the mypy setting

This decorator settings currently raise a mypy error. To avoid this error, please set the `--disable-error-code misc` option.

See also:

- [Recommended type annotation checker settings](recommended_type_checker_settings.md)

## See also

- [set_debug_mode interface](set_debug_mode.md)
- [unset_debug_mode interface](unset_debug_mode.md)