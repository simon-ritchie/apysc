"""Test project for MouseEvent class.

Command examples:
$ python test_projects/MouseEvent/main.py
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
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)
    stage_elem_id: str = stage.stage_elem_id
    stage_elem_str: str = f'$("#{stage_elem_id}")'
    ap.append_js_expression(
        f'{stage_elem_str}.css("margin-left", "150px");')

    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=100, width=50, height=50)
    rectangle_1.click(on_rectangle_1_clicked)

    sprite_2: ap.Sprite = ap.Sprite(stage=stage)
    sprite_2.graphics.begin_fill(color='#f0a')
    sprite_2.x = ap.Int(150)
    sprite_2.y = ap.Int(100)
    rectangle_2: ap.Rectangle = sprite_2.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_2.click(on_rectangle_2_clicked)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_rectangle_1_clicked(e: ap.MouseEvent, options: dict) -> None:
    """
    Test handler that called when rectangle_1 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Rectangle 1 clicked!')
    ap.trace('stage_x:', e.stage_x)
    ap.assert_true(e.stage_x >= ap.Int(50))
    ap.assert_true(e.stage_x <= ap.Int(100))

    ap.trace('stage_y:', e.stage_y)
    ap.assert_true(e.stage_y >= ap.Int(100))
    ap.assert_true(e.stage_y <= ap.Int(150))

    ap.trace('local_x:', e.local_x)
    ap.assert_true(e.local_x >= ap.Int(0))
    ap.assert_true(e.local_x <= ap.Int(50))


def on_rectangle_2_clicked(e: ap.MouseEvent, options: dict) -> None:
    """
    Test handler that called when rectangle_2 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Rectangle 2 clicked!')
    ap.trace('local_x:', e.local_x)
    ap.assert_true(e.local_x >= ap.Int(0))
    ap.assert_true(e.local_x <= ap.Int(50))

    ap.trace('local_y:', e.local_y)
    ap.assert_true(e.local_y >= ap.Int(0))
    ap.assert_true(e.local_y <= ap.Int(50))


if __name__ == '__main__':
    main()
