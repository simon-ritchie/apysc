# Material icons

This page explains the material icon-related implementations of apysc.

## Implementation overview

Each material icon class name becomes the `Material<icon_name>Icon`, for instance, `MaterialSearchIcon` or `MaterialAccountCircleIcon`.

You can use these icon classes similar to the other graphics classes, such as the `Rectangle` or `Circle`.

## Basic usage

```py
# runnable
import apysc as ap

MARGIN: int = 20
ICON_SIZE: int = 24
ICON_NUM: int = 3
stage: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=MARGIN * 2 + ICON_SIZE * ICON_NUM + MARGIN * 2,
    stage_height=MARGIN + ICON_SIZE + MARGIN,
    stage_elem_id="stage",
)

search_icon: ap.MaterialSearchIcon = ap.MaterialSearchIcon(
    fill_color=ap.Colors.GRAY_AAAAAA,
    x=MARGIN,
    y=MARGIN,
    width=ICON_SIZE,
    height=ICON_SIZE,
)
info_icon: ap.MaterialInfoIcon = ap.MaterialInfoIcon(
    fill_color=ap.Colors.CYAN_00FFFF,
    x=MARGIN + ICON_SIZE + MARGIN,
    y=MARGIN,
    width=ICON_SIZE,
    height=ICON_SIZE,
)
home_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(
    fill_color=ap.Colors.MAGENTA_FF00FF,
    x=MARGIN + (ICON_SIZE + MARGIN) * 2,
    y=MARGIN,
    width=ICON_SIZE,
    height=ICON_SIZE,
)

ap.save_overall_html(dest_dir_path="./material_icons_basic_usage/")
```

<iframe src="static/material_icons_basic_usage/index.html" width="152" height="64"></iframe>

## Each material icon constructor API

<!-- Docstring: apysc._material_design.icon.path_and_var_name_setting_base.PathAndVarNameSettingBase.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, fill_color: apysc._color.color.Color, fill_alpha: Union[float, apysc._type.number.Number] = 1.0, x: Union[float, apysc._type.number.Number] = 0, y: Union[float, apysc._type.number.Number] = 0, width: Union[int, apysc._type.int.Int] = 24, height: Union[int, apysc._type.int.Int] = 24, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Create a material icon.<hr>

**[Parameters]**

- `fill_color`: Color
  - An icon fill-color.
- `fill_alpha`: Union[float, Number], optional
  - An icon fill-alpha (opacity).
- `x`: Union[float, Number], optional
  - An icon x-coordinate.
- `y`: Union[float, Number], optional
  - An icon y-coordinate.
- `width`: Union[int, Int], optional
  - An icon width.
- `height`: Union[int, Int], optional
  - An icon height.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[References]**

- [Material icons](https://fonts.google.com/icons?selected=Material+Icons:search:)
- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)