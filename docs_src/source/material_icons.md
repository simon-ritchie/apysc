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