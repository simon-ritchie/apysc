"""The test project for the delete interface.

Command examples:
$ python test_projects/delete/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


class _Options(TypedDict):
    sprite: ap.Sprite


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage()
    ap.set_debug_mode()
    int_1: ap.Int = ap.Int(10)
    ap.delete(int_1)
    ap.assert_undefined(int_1)

    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color=ap.Color("#0af"))
    sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

    options: _Options = {"sprite": sprite}
    ap.Timer(on_timer, delay=3000, repeat_count=1, options=options).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer(e: ap.TimerEvent, options: _Options) -> None:
    """
    The handler that a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _Options
        Optional arguments dictionary.
    """
    ap.delete(value=options["sprite"])
    ap.assert_undefined(options["sprite"])


if __name__ == "__main__":
    main()
