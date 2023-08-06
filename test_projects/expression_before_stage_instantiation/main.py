"""The test project for the expression before stage instantiation.

Command examples:
$ python test_projects/expression_before_stage_instantiation/main.py
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

TEST_INT_1: ap.Int = ap.Int(100)
TEST_INT_2: ap.Int = ap.Int(200)
TEST_STRING_1: ap.String = ap.String("Hello")
TEST_STRING_2: ap.String = ap.String("World")
TEST_BOOL_1: ap.Boolean = ap.Boolean(True)
TEST_BOOL_2: ap.Boolean = ap.Boolean(False)
TEST_NUMBER_1: ap.Number = ap.Number(10.5)
TEST_NUMBER_2: ap.Number = ap.Number(20.5)
TEST_ARRAY_1: ap.Array = ap.Array([1, 2, 3])
TEST_ARRAY_2: ap.Array = ap.Array([ap.Int(4), ap.Int(5), ap.Int(6)])
TEST_DICT_1: ap.Dictionary = ap.Dictionary({"a": 1, "b": 2})
TEST_DICT_2: ap.Dictionary = ap.Dictionary({"c": ap.Int(3), "d": ap.Int(4)})


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1200,
        stage_height=900,
    )

    ap.assert_equal(TEST_INT_1, 100)
    ap.assert_equal(TEST_INT_2, 200)
    ap.assert_equal(TEST_STRING_1, "Hello")
    ap.assert_equal(TEST_STRING_2, "World")
    ap.assert_equal(TEST_BOOL_1, True)
    ap.assert_equal(TEST_BOOL_2, False)
    ap.assert_equal(TEST_NUMBER_1, 10.5)
    ap.assert_equal(TEST_NUMBER_2, 20.5)
    ap.assert_arrays_equal(TEST_ARRAY_1, [1, 2, 3])
    ap.assert_arrays_equal(TEST_ARRAY_2, [4, 5, 6])
    ap.assert_dicts_equal(TEST_DICT_1, {"a": 1, "b": 2})
    ap.assert_dicts_equal(TEST_DICT_2, {ap.String("c"): 3, ap.String("d"): 4})

    int_value: ap.Int = ap.Int(30)
    ap.assert_equal(int_value, 30)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
