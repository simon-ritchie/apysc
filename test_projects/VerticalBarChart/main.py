"""The test project for the `VerticalBarChart` class.

Command examples:
$ python test_projects/VerticalBarChart/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._chart.vertical_bar_chart import VerticalBarChart
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )

    x_axis_settings: ap.XAxisSettings = ap.XAxisSettings(
        x_axis_column_name="date",
    )
    y_axis_settings: ap.YAxisSingleColumnSettings = ap.YAxisSingleColumnSettings(
        y_axis_column_name="value",
        tick_text_fill_color=ap.Color("#aaa"),
        tick_text_font_size=10,
    )
    _: VerticalBarChart = VerticalBarChart(
        data=[
            {"value": 10, "date": "2023-01-01"},
            {"value": 20, "data": "2023-01-02"},
            {"value": 40, "data": "2023-01-03"},
            {"value": 5.5, "data": "2023-01-03"},
        ],
        x_axis_settings=x_axis_settings,
        y_axis_settings=y_axis_settings,
        x=100,
        y=150,
        width=500,
        height=300,
        background_fill_color=ap.Color("#555"),
        background_fill_alpha=0.7,
        border_color=ap.Color("#666"),
        border_alpha=1,
        border_thickness=1,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
