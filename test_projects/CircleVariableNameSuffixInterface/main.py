"""The test project for the Circle class's VariableNameSuffixInterface.

Command examples:
$ python test_projects/CircleVariableNameSuffixInterface/main.py
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

    ap.Circle = ap.Circle(
        x=100, y=100, radius=50, fill_color='#0af',
        variable_name_suffix='circle_1')

    sprite: ap.Sprite = ap.Sprite(variable_name_suffix='sprite_1')
    sprite.graphics.begin_fill(color='#f0a', alpha=0.5)
    sprite.graphics.line_style(
        color='#fff', thickness=3, alpha=0.7)
    sprite.graphics.draw_circle(
        x=300, y=100, radius=75, variable_name_suffix='circle_2')

    ap.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH,
        minify=False)


if __name__ == '__main__':
    main()
