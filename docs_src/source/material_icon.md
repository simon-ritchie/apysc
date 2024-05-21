# Material icon

This page explains the material icon's apysc implementations.

## Basic usage

Each material icon exists in the root package (e.g., `ap.MaterialTimelineIcon`).

Also, each material icon name has the prefix of `Material` and suffix of `Icon`.

All material icons' constructor has the coordinates and style settings arguments, such as the `x`, `y`, `size`, `fill_color`, and `fill_alpha`.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=168,
    stage_height=72,
    stage_elem_id="stage",
)
SIZE: int = 24

ap.MaterialHomeIcon(
    x=24,
    y=24,
    size=SIZE,
    fill_color=ap.Colors.CYAN_00AAFF,
)
ap.MaterialBuildIcon(
    x=24 * 3,
    y=24,
    size=SIZE,
    fill_color=ap.Colors.CYAN_00AAFF,
)
ap.MaterialCheckCircleIcon(
    x=24 * 5,
    y=24,
    size=SIZE,
    fill_color=ap.Colors.CYAN_00AAFF,
)

ap.save_overall_html(dest_dir_path="material_icon_basic_usage_1/")
```

<iframe src="static/material_icon_basic_usage_1/index.html" width="168" height="72"></iframe>

You can also set coordinates or styles with an instance's attributes as follows:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=168,
    stage_height=72,
    stage_elem_id="stage",
)
SIZE: int = 24

home_icon: ap.MaterialHomeIcon = ap.MaterialHomeIcon(size=SIZE)
home_icon.x = ap.Number(24)
home_icon.y = ap.Number(24)
home_icon.fill_color = ap.Colors.CYAN_00AAFF

build_icon: ap.MaterialBuildIcon = ap.MaterialBuildIcon(size=SIZE)
build_icon.x = ap.Number(24 * 3)
build_icon.y = ap.Number(24)
build_icon.fill_color = ap.Colors.CYAN_00AAFF

check_circle_icon: ap.MaterialCheckCircleIcon = ap.MaterialCheckCircleIcon(
    size=SIZE,
)
check_circle_icon.x = ap.Number(24 * 5)
check_circle_icon.y = ap.Number(24)
check_circle_icon.fill_color = ap.Colors.CYAN_00AAFF

ap.save_overall_html(dest_dir_path="material_icon_basic_usage_2/")
```

<iframe src="static/material_icon_basic_usage_2/index.html" width="168" height="72"></iframe>

## Material icon's license

The apysc library uses material icons licensed under the APACHE LICENSE, VERSION 2.0.

- [Material Symbols & Icons](https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed)
- [material-design-icons (GitHub)](https://github.com/google/material-design-icons)
- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)

## Each material icon constructor API

<!-- Docstring: apysc._display.fixed_html_svg_icon_base.FixedHtmlSvgIconBase.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, x: Union[float, apysc._type.number.Number] = 0.0, y: Union[float, apysc._type.number.Number] = 0.0, size: Union[int, apysc._type.int.Int] = 24, fill_color: apysc._color.color.Color = Color("#666666"), fill_alpha: Union[float, apysc._type.number.Number] = 1.0, parent: Union[apysc._display.child_mixin.ChildMixIn, NoneType] = None, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

The class implementation for the SVG icon's class.<hr>

**[Parameters]**

- `x`: Union[float, Number], optional
  - X-coordinate of the icon.
- `y`: Union[float, Number], optional
  - Y-coordinate of the icon.
- `size`: Union[int, Int], optional
  - Size of the icon.
- `fill_color`: Color, optional
  - Fill-color of the icon.
- `fill_alpha`: Union[float, Number], optional
  - Fill-alpha of the icon.
- `parent`: Optional[ChildMixIn], optional
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.