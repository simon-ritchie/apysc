"""The test project for the Line class's VariableNameSuffixInterface.

Command examples:
$ python test_projects/LineVariableNameSuffixInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage',
        variable_name_suffix='stage')

    ap.Line(
        start_point=ap.Point2D(x=50, y=50),
        end_point=ap.Point2D(x=150, y=50),
        line_color='#0af', line_thickness=3,
        variable_name_suffix='line_1')

    sprite: ap.Sprite = ap.Sprite(variable_name_suffix='sprite_1')
    sprite.graphics.line_style(
        color='#fff', thickness=3, alpha=0.7)
    sprite.graphics.draw_line(
        x_start=50, y_start=100, x_end=150, y_end=100,
        variable_name_suffix='line_2')

    ap.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH,
        minify=False)


if __name__ == '__main__':
    main()
