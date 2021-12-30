"""The test project for the draw_rect interface.

Command examples:
$ python test_projects/draw_rect/main.py
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
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    ap.set_debug_mode()

    # Basic functional test case.
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color='#00aaff')
    sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    stage.add_child(child=sprite)

    # Test for begin_fill interface.
    sprite.graphics.begin_fill(color='#00aaff', alpha=0.5)
    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

    # Test for line_style interface.
    sprite.graphics.begin_fill(color='#00aaff')
    sprite.graphics.line_style(color='#fff', thickness=3, alpha=0.7)
    sprite.graphics.draw_rect(x=250, y=50, width=50, height=50)

    # Test for rectangle x position update.
    rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        x=0, y=50, width=50, height=50)
    rectangle.x = ap.Int(350)

    # Test for rectangle y position update.
    rectangle = sprite.graphics.draw_rect(
        x=450, y=0, width=50, height=50)
    rectangle.y = ap.Int(50)

    # Test for rectangle width update.
    rectangle = sprite.graphics.draw_rect(
        x=550, y=50, width=50, height=50)
    rectangle.width = ap.Int(100)

    # Test for rectangle height update.
    rectangle = sprite.graphics.draw_rect(
        x=700, y=50, width=50, height=50)
    rectangle.height = ap.Int(100)

    # Test for rectangle fill color update.
    rectangle = sprite.graphics.draw_rect(
        x=800, y=50, width=50, height=50)
    rectangle.fill_color = ap.String('#f0a')

    # Test for rectangle fill alpha update.
    rectangle = sprite.graphics.draw_rect(
        x=900, y=50, width=50, height=50)
    rectangle.fill_alpha = ap.Number(0.5)

    # Test for rectangle line color update.
    rectangle = sprite.graphics.draw_rect(
        x=50, y=150, width=50, height=50)
    rectangle.line_color = ap.String('#f0a')

    # Test for rectangle line thickness update.
    rectangle = sprite.graphics.draw_rect(
        x=150, y=150, width=50, height=50)
    rectangle.line_thickness = ap.Int(1)

    # Test for rectangle line alpha update.
    rectangle = sprite.graphics.draw_rect(
        x=250, y=150, width=50, height=50)
    rectangle.line_alpha = ap.Number(1.0)

    _another_func(stage=stage, sprite=sprite)

    sprite.graphics.draw_rect(
        x=450, y=150, width=50, height=50)

    # Test for rectangle fill alpha update with Number.
    number_1: ap.Number = ap.Number(0.725)
    rectangle = sprite.graphics.draw_rect(
        x=550, y=150, width=50, height=50)
    rectangle.fill_alpha = number_1

    # Test for each attribute values are immutable.
    rectangle.fill_alpha = ap.Number(0.5)
    fill_alpha: ap.Number = rectangle.fill_alpha
    fill_alpha += 0.2
    ap.assert_not_equal(left=fill_alpha, right=rectangle.fill_alpha)

    rectangle.x = ap.Int(550)
    x: ap.Int = rectangle.x
    x += 100
    ap.assert_not_equal(left=x, right=rectangle.x)

    rectangle.y = ap.Int(150)
    y: ap.Int = rectangle.y
    y += 100
    ap.assert_not_equal(left=y, right=rectangle.y)

    rectangle.line_thickness = ap.Int(2)
    line_thickness: ap.Int = rectangle.line_thickness
    line_thickness += 1
    ap.assert_not_equal(
        left=line_thickness, right=rectangle.line_thickness)

    rectangle.line_alpha = ap.Number(0.5)
    line_alpha: ap.Number = rectangle.line_alpha
    line_alpha += 0.2
    ap.assert_not_equal(left=line_alpha, right=rectangle.line_alpha)

    width: ap.Int = rectangle.width
    width = ap.Int(150)
    ap.assert_not_equal(left=width, right=rectangle.width)

    height: ap.Int = rectangle.height
    height = ap.Int(200)
    ap.assert_not_equal(left=height, right=rectangle.height)

    sprite.graphics.line_style(
        color='#fff', thickness=5, dot_setting=ap.LineDotSetting(dot_size=5))
    rectangle = sprite.graphics.draw_rect(
        x=650, y=150, width=50, height=50)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def _another_func(stage: ap.Stage, sprite: ap.Sprite) -> None:
    """
    Another function to test expression and arguments behavior.

    Parameters
    ----------
    stage : Stage
        Stage instance.
    sprite : Sprite
        Sprite instance.
    """
    sprite.graphics.begin_fill(color='#f0a')
    sprite.graphics.draw_rect(x=350, y=150, width=50, height=50)
    stage.add_child(child=sprite)


if __name__ == '__main__':
    main()
