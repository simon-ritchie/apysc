# MaterialDesignColors class

This page explains the `MaterialDesignColors` class.

## What class is this?

The `MaterialDesignColors` class has material design's `Color` constants, such as the `RED_100_FFCDD2`, `RED_300_E57373`, `INDIGO_800_283593`, and `INDIGO_A200_536DFE`.

Each suffix is a hexadecimal color code of its color.

## Basic usage

These class constants behave the same as a `Color` value.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.MaterialDesignColors.GRAY_800_424242,
    stage_elem_id="stage",
)

rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.MaterialDesignColors.CYAN_200_80DEEA,
    line_color=ap.MaterialDesignColors.WHITE_FFFFFF,
    line_thickness=3,
)

ap.save_overall_html(dest_dir_path="./material_design_colors_basic_usage/")
```

<iframe src="static/material_design_colors_basic_usage/index.html" width="150" height="150"></iframe>

## Defined colors

<br>
<details>
<summary>Display the code block:</summary>

```py
# runnable
from typing import List, Tuple

import apysc as ap

RECT_SIZE: int = 25
FONT_SIZE: int = 12
OUTER_MARGIN: int = 20
_: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=700,
    stage_height=((len(ap.MaterialDesignColors.get_colors_members()) + 1) // 2)
    * (RECT_SIZE + 10)
    + OUTER_MARGIN * 2
    - 10,
)

color: ap.Color
colors_members: List[
    Tuple[str, ap.Color]
] = ap.MaterialDesignColors.get_colors_members()
color_names: List[ap.String] = []
colors: List[ap.Color] = []
for color_name, color in colors_members:
    color_names.append(ap.String(color_name))
    colors.append(color)
constant_names_arr: ap.Array[ap.String] = ap.Array(color_names)
colors_arr: ap.Array[ap.Color] = ap.Array(colors)

i: ap.Int
x: ap.Number = ap.Number(0)
y: ap.Number = ap.Number(0)
with ap.ForArrayIndices(constant_names_arr) as i:
    with ap.If(i % 2 == 0):
        x.value = OUTER_MARGIN
    with ap.Else():
        x.value = 350
    y.value = (i // 2) * (RECT_SIZE + 10) + 20
    color = colors_arr[i]
    constant_name: ap.String = constant_names_arr[i]
    ap.Rectangle(
        x=x,
        y=y,
        width=RECT_SIZE,
        height=RECT_SIZE,
        fill_color=color,
        line_color=ap.Color("#fff"),
        line_thickness=1,
        line_alpha=0.5,
    )
    ap.SVGText(
        text=constant_name,
        x=x + RECT_SIZE + 10,
        y=y + RECT_SIZE / 2 + FONT_SIZE / 2 - 2,
        font_size=FONT_SIZE,
        fill_color=ap.Color("#ccc"),
    )

ap.save_overall_html(dest_dir_path="./material_design_colors_definitions/")
```

</details>

<iframe src="static/material_design_colors_definitions/index.html" width="700" height="4510"></iframe>

## References

- [Overview, Material Design](https://m3.material.io/styles/color/overview)
- [Style, Material Design](https://m1.material.io/style/color.html#)