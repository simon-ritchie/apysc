"""Test project for draw_rect interface.

Command example:
$ python test_projects/draw_rect/main.py
"""

import sys

sys.path.append('./')

from types import ModuleType

from apyscript.decorator.update_current_scope import update_current_scope
from apyscript.display.rectangle import Rectangle
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage

this_module: ModuleType = sys.modules[__name__]


@update_current_scope(module=this_module)
def main() -> None:
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)

    # Basic functional test case.
    sprite: Sprite = Sprite(stage=stage)
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
    rectangle: Rectangle = sprite.graphics.draw_rect(
        x=0, y=50, width=50, height=50)
    rectangle.x = 350

    # Test for rectangle y position update.
    rectangle = sprite.graphics.draw_rect(
        x=450, y=0, width=50, height=50)
    rectangle.y = 50

    # Test for rectangle width update.
    rectangle = sprite.graphics.draw_rect(
        x=550, y=50, width=50, height=50)
    rectangle.width = 100

    # Test for rectangle height update.
    rectangle = sprite.graphics.draw_rect(
        x=700, y=50, width=50, height=50)
    rectangle.height = 100

    # Test for rectangle fill color update.
    rectangle = sprite.graphics.draw_rect(
        x=800, y=50, width=50, height=50)
    rectangle.fill_color = '#f0a'

    # Test for rectangle fill alpha update.
    rectangle = sprite.graphics.draw_rect(
        x=900, y=50, width=50, height=50)
    rectangle.fill_alpha = 0.5

    # Test for rectangle line color update.
    rectangle = sprite.graphics.draw_rect(
        x=50, y=150, width=50, height=50)
    rectangle.line_color = '#f0a'

    # Test for rectangle line thickness update.
    rectangle = sprite.graphics.draw_rect(
        x=150, y=150, width=50, height=50)
    rectangle.line_thickness = 1

    # Test for rectangle line alpha update.
    rectangle = sprite.graphics.draw_rect(
        x=250, y=150, width=50, height=50)
    rectangle.line_alpha = 1.0

    _another_func(stage=stage, sprite=sprite)

    sprite.graphics.draw_rect(
        x=450, y=150, width=50, height=50)


def _another_func(stage: Stage, sprite: Sprite) -> None:
    sprite.graphics.begin_fill(color='#f0a')
    sprite.graphics.draw_rect(x=350, y=150, width=50, height=50)
    stage.add_child(child=sprite)


if __name__ == '__main__':
    main()
