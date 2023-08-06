"""The test project for the `ForDictKeysAndValues` class.

Command examples:
$ python test_projects/ForDictKeysAndValues/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(background_color=ap.Color("#333"), stage_width=250, stage_height=300)

    dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(
        {
            ap.Number(50): ap.Number(50),
            ap.Number(100): ap.Number(125),
            ap.Number(150): ap.Number(200),
        }
    )
    with ap.ForDictKeysAndValues(
        dict_=dict_,
        dict_key_type=ap.Number,
        dict_value_type=ap.Number,
    ) as (key, value):
        ap.Rectangle(x=key, y=value, width=50, height=50, fill_color=ap.Color("#0af"))

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
