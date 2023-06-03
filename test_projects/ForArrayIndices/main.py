"""The test project for the `ForArrayIndices` class.

Command examples:
$ python test_projects/ForArrayIndices/main.py
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
    ap.Stage(background_color="#333", stage_width=1000, stage_height=500)

    arr: ap.Array[ap.Number] = ap.Array(
        [ap.Number(50), ap.Number(150), ap.Number(250)]
    )
    indices: ap.Array[ap.Int] = ap.Array([])
    with ap.ForArrayIndices(arr=arr) as i:
        indices.append(i)
        x: ap.Number = arr[i]
        ap.Circle(x=x, y=150, radius=20, fill_color="#00aaff")

    ap.assert_arrays_equal(
        indices,
        [0, 1, 2],
    )
    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
