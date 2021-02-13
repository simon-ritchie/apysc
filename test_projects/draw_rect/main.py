"""Test project for draw_rect interface.

Command example:
$ python test_projects/draw_rect/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.decorator.update_current_scope import update_current_scope
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


@update_current_scope(module=this_module)
def main() -> None:
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(
        background_color='#111',
        stage_width=500, stage_height=300)
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#00aaff')
    sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    stage.add_child(child=sprite)

    sprite.graphics.begin_fill(color='#00aaff', alpha=0.5)
    sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
