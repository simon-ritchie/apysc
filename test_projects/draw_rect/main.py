"""Test project for draw_rect interface.
"""

import sys
sys.path.append('./')

import os
from types import ModuleType

from apyscript.display.stage import Stage
from apyscript.html import exporter
from apyscript.file import file_util
from apyscript.display.sprite import Sprite

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(background_color='#111')
    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#00aaff')
    stage.add_child(child=sprite)


if __name__ == '__main__':
    main()
