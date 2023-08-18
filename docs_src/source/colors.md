# Colors class

This page explains the `Colors` class.

## What class is this?

The `Colors` class has `Color` constants, such as the `BLACK_000000`, `GRAY_999999`, `WHITE_FFFFFF`, and `RED_FF0000`.

Each suffix is a hexadecimal color code of its color.

## Basic usage

These class constants behave the same as a `Color` value.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Colors.GRAY_333333,
    stage_elem_id="stage",
)

rectangle: ap.Rectangle = ap.Rectangle(
    x=50,
    y=50,
    width=50,
    height=50,
    fill_color=ap.Colors.CYAN_00FFFF,
    line_color=ap.Colors.WHITE_FFFFFF,
    line_thickness=3,
)

ap.save_overall_html(dest_dir_path="./colors_basic_usage/")
```

<iframe src="static/colors_basic_usage/index.html" width="150" height="150"></iframe>

## Defined colors

`ap.Colors`:

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

RECT_SIZE: int = 25
FONT_SIZE: int = 12
OUTER_MARGIN: int = 20
_: ap.Stage = ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=450,
    stage_height=(len(ap.Colors.get_colors_members()) // 2) * (RECT_SIZE + 10)
    + OUTER_MARGIN * 2
    - 10,
)

i: int
constant_name: str
color: ap.Color
for i, (constant_name, color) in enumerate(ap.Colors.get_colors_members()):
    if i % 2 == 0:
        x = 20
    else:
        x = 250
    y: int = (i // 2) * (RECT_SIZE + 10) + 20
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

ap.save_overall_html(dest_dir_path="./colors_definitions/")
```

</details>

<iframe src="static/colors_definitions/index.html" width="450" height="415"></iframe>