import importlib
import os
import re
import shutil
import time
import traceback
from random import randint
from types import ModuleType
from typing import Callable
from typing import Dict
from typing import List
from typing import Match
from typing import Optional
from typing import Type

from apysc._file import file_util
from apysc._file import module_util
from apysc._lint_and_doc import docstring_to_markdown_converter
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._testing.testing_helper import apply_test_settings

_MODULE_STR: str = '''"""Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Notes
-----
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.

References
----------
- Duis aute irure dolor in reprehenderit in voluptate
    - https://simon-ritchie.github.io/apysc/en/test_doc_1.html
- Velit esse cillum dolore eu fugiat nulla pariatur
    - https://simon-ritchie.github.io/apysc/en/test_doc_2.html
"""

import os
from multiprocessing import Process
from multiprocessing import cpu_count


def sample_func_1(a: int, b: bool) -> str:
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore
    magna aliqua.

    Parameters
    ----------
    a : int
        cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.
    b : bool
        At vero eos et accusamus et iusto odio dignissimos.

    Returns
    -------
    c : str
        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt.
    d : float
        cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.

    Notes
    -----
    Duis aute irure dolor in reprehenderit in voluptate.

    - Cupidatat non proident, sunt in culpa qui officia.
    - Deserunt mollit anim id est laborum.

    Examples
    --------
    >>> a: int = 10
    >>> b: int = a + 20
    >>> b
    30

    References
    ----------
    - Duis aute irure dolor in reprehenderit in voluptate
        - https://simon-ritchie.github.io/apysc/en/test_doc_3.html
    - Velit esse cillum dolore eu fugiat nulla pariatur
        - https://simon-ritchie.github.io/apysc/en/test_doc_4.html

    Raises
    ------
    ValueError
        Lorem ipsum dolor sit amet, consectetur adipiscing.
    """
    ...


class _SampleClass(Process):
    """Cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum.
    """

    def __init__(self) -> None:
        """Cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.
        """
        ...

    def sample_method_1(self, e: int) -> str:
        """
        Cupidatat non proident, sunt in culpa qui officia.

        Parameters
        ----------
        e : int
            Lorem ipsum dolor sit amet, consectetur adipiscing
            elit, sed do eiusmod tempor incididunt.

        Returns
        -------
        d : str
            Velit esse cillum dolore eu fugiat nulla pariatur.
        """
        ...
'''

_test_module_dir_path: str = ""
_test_module_path: str = ""


def _update_test_dir_and_module_paths() -> None:
    """
    Update test directory and module paths.
    """
    global _test_module_dir_path, _test_module_path
    random_int: int = randint(0, 1000000000)
    _test_module_dir_path = f"./tmp/test_docstring_to_markdown_converter_{random_int}/"
    _test_module_path = os.path.join(_test_module_dir_path, "test_module_1.py")


def _read_test_module() -> ModuleType:
    """
    Read a module for testing.

    Returns
    -------
    module : ModuleType
        Read module.
    """
    global _test_module_path
    count: int = 0
    while True:
        try:
            _save_test_module()
            module: ModuleType = module_util.read_target_path_module(
                module_path=_test_module_path
            )
            importlib.reload(module)
            break
        except Exception:
            traceback_: str = traceback.format_exc()
            time.sleep(randint(1, 2))
            count += 1
        if count > 3:
            print(traceback_)
            raise Exception("Failed to read a module for testing.")
        continue
    return module


def _save_test_module() -> None:
    """Save the test module."""
    global _test_module_dir_path, _test_module_path
    _update_test_dir_and_module_paths()
    os.makedirs("./tmp/", exist_ok=True)
    file_util.append_plain_txt(txt="", file_path="./tmp/__init__.py")
    os.makedirs(_test_module_dir_path, exist_ok=True)
    init_path: str = os.path.join(_test_module_dir_path, "__init__.py")
    file_util.save_plain_txt(txt="", file_path=init_path)
    file_util.save_plain_txt(txt=_MODULE_STR, file_path=_test_module_path)


@apply_test_settings()
def _remove_test_module_dir() -> None:
    """Remove the test modules directory."""
    global _test_module_dir_path
    shutil.rmtree(_test_module_dir_path, ignore_errors=True)


def teardown() -> None:
    _remove_test_module_dir()


@apply_test_settings()
def test__append_module_docstring_to_markdown() -> None:
    _save_test_module()
    markdown: str = (
        docstring_to_markdown_converter._append_module_docstring_to_markdown(
            markdown="", docstring=None
        )
    )
    assert markdown == ""

    module: ModuleType = _read_test_module()
    markdown = docstring_to_markdown_converter._append_module_docstring_to_markdown(
        markdown="# Test module docstring", docstring=module.__doc__
    )
    expected_strs: List[str] = [
        "# Test module docstring\n\n",
        "## Module summary\n\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing "
        "elit, sed do eiusmod tempor incididunt ut labore et "
        "dolore magna aliqua.<hr>\n\n",
        "**[Notes]**\n\n",
        "**[References]**\n\n",
    ]
    for expected_str in expected_strs:
        assert expected_str in markdown


@apply_test_settings()
def test__get_module_toplevel_functions() -> None:
    module: ModuleType = _read_test_module()
    toplevel_functions: List[Callable] = (
        docstring_to_markdown_converter._get_module_toplevel_functions(module=module)
    )
    assert len(toplevel_functions) == 1
    assert toplevel_functions[0].__name__ == "sample_func_1"


@apply_test_settings()
def test__append_toplevel_function_docstring_to_markdown() -> None:
    markdown: str = (
        docstring_to_markdown_converter._append_toplevel_function_docstring_to_markdown(
            markdown="",
            toplevel_function=(test__append_toplevel_function_docstring_to_markdown),
        )
    )
    assert markdown == ""

    module: ModuleType = _read_test_module()
    toplevel_functions: List[Callable] = (
        docstring_to_markdown_converter._get_module_toplevel_functions(module=module)
    )
    markdown = (
        docstring_to_markdown_converter._append_toplevel_function_docstring_to_markdown(
            markdown="# Test docstring\n\nLorem ipsum dolor.",
            toplevel_function=toplevel_functions[0],
        )
    )
    expected_strs: List[str] = [
        "# Test docstring\n\nLorem ipsum dolor.\n\n",
        f"## `{toplevel_functions[0].__name__}` function docstring",
        "**[Parameters]**",
    ]
    for expected_str in expected_strs:
        assert expected_str in markdown


@apply_test_settings()
def test__append_each_section_to_markdown() -> None:
    module: ModuleType = _read_test_module()
    toplevel_functions: List[Callable] = (
        docstring_to_markdown_converter._get_module_toplevel_functions(module=module)
    )
    docstring: str = toplevel_functions[0].__doc__ or ""
    markdown = docstring_to_markdown_converter._append_each_section_to_markdown(
        markdown="## Test docstring\n\nLorem ipsum dolor.", docstring=docstring
    )
    expected_strs: List[str] = [
        "## Test docstring\n\nLorem ipsum dolor.\n\n",
        "**[Parameters]**",
        "**[Returns]**",
        "**[Raises]**",
        "**[Notes]**",
        "**[Examples]**",
        "**[References]**",
    ]
    for expected_str in expected_strs:
        assert expected_str in markdown


@apply_test_settings()
def test__get_toplevel_classes() -> None:
    module: ModuleType = _read_test_module()
    toplevel_classes: List[Type] = (
        docstring_to_markdown_converter._get_toplevel_classes(module=module)
    )
    assert len(toplevel_classes) == 2
    names: List[str] = [toplevel_class.__name__ for toplevel_class in toplevel_classes]
    assert sorted(names) == sorted(["Process", "_SampleClass"])


@apply_test_settings()
def test__get_methods_from_class() -> None:
    module: ModuleType = _read_test_module()
    toplevel_classes: List[Type] = (
        docstring_to_markdown_converter._get_toplevel_classes(module=module)
    )
    target_class: Optional[Type] = None
    for toplevel_class in toplevel_classes:
        if toplevel_class.__name__ == "_SampleClass":
            target_class = toplevel_class
            break
    if target_class is None:
        raise AssertionError(f"Returned values are invalid: {toplevel_classes}")
    methods: List[Callable] = docstring_to_markdown_converter._get_methods_from_class(
        class_=target_class
    )
    assert len(methods) >= 2
    for method in methods:
        assert callable(method)
    actual_method_names: List[str] = [method.__name__ for method in methods]
    assert "__init__" in actual_method_names
    assert "sample_method_1" in actual_method_names


@apply_test_settings()
def test__append_toplevel_class_docstring_to_markdown() -> None:
    module: ModuleType = _read_test_module()
    toplevel_classes: List[Type] = (
        docstring_to_markdown_converter._get_toplevel_classes(module=module)
    )
    target_class: Optional[Type] = None
    for toplevel_class in toplevel_classes:
        if toplevel_class.__name__ == "_SampleClass":
            target_class = toplevel_class
            break
    if target_class is None:
        raise AssertionError(f"Returned values are invalid: {toplevel_classes}")
    markdown: str = (
        docstring_to_markdown_converter._append_toplevel_class_docstring_to_markdown(
            markdown="# Test docstring\n\nLorem ipsum dolor.",
            toplevel_class=target_class,
            module_str=_MODULE_STR,
        )
    )
    expected_strs: List[str] = [
        "# Test docstring\n\nLorem ipsum dolor.\n\n",
        "## `_SampleClass` class docstring\n\n" "Cupidatat non proident",
        "## `__init__` method docstring\n\n",
        "## `sample_method_1` method docstring\n\n",
        "**[Parameters]**",
    ]
    for expected_str in expected_strs:
        assert expected_str in markdown

    assert "## close method docstring" not in markdown


@apply_test_settings()
def test__convert_module_docstring_to_markdown() -> None:
    global _test_module_path
    _save_test_module()
    markdown: str = (
        docstring_to_markdown_converter._convert_module_docstring_to_markdown(
            module_path=_test_module_path
        )
    )
    expected_strs: List[str] = [
        "# `tmp.test_docstring_to_markdown_converter_",
        "test_module_1` docstrings",
        "## Module summary",
        "## `sample_func_1` function docstring",
        "## `_SampleClass` class docstring",
        "### `__init__` method docstring",
        "### `sample_method_1` method docstring",
    ]
    for expected_str in expected_strs:
        assert expected_str in markdown

    unexpected_strs: List[str] = [
        "Process",
        "cpu_count",
    ]
    for unexpected_str in unexpected_strs:
        assert unexpected_str not in markdown


@apply_test_settings()
def test__save_markdown() -> None:
    global _test_module_path
    _save_test_module()
    markdown_file_path: str = docstring_to_markdown_converter._save_markdown(
        module_path=_test_module_path,
    )
    match: Optional[Match] = re.match(
        pattern=(
            r"./docstring_markdowns/tmp/test_docstring_to_markdown_converter"
            r".*?/test_module_1.md"
        ),
        string=markdown_file_path,
    )
    assert match is not None
    assert os.path.isfile(markdown_file_path)
    markdown: str = file_util.read_txt(file_path=markdown_file_path)
    match = re.search(
        pattern=(
            r"# `tmp\.test_docstring_to_markdown_converter.*?"
            r"\.test_module_1` docstrings"
        ),
        string=markdown,
    )
    assert match is not None

    shutil.rmtree("./docstring_markdowns/tmp/", ignore_errors=True)


@apply_test_settings()
def test_convert_recursively() -> None:
    global _test_module_dir_path, _test_module_path
    _save_test_module()
    shutil.rmtree("./docstring_markdowns/tmp/", ignore_errors=True)
    subdir_path: str = os.path.join(
        _test_module_dir_path,
        "subdir/",
    )
    os.makedirs(subdir_path, exist_ok=True)
    txt_path: str = os.path.join(
        _test_module_dir_path,
        "test.txt",
    )
    file_util.save_plain_txt(txt="test", file_path=txt_path)
    init_path: str = os.path.join(_test_module_dir_path, "__init__.py")

    saved_markdown_file_paths: List[str] = (
        docstring_to_markdown_converter.convert_recursively(
            dir_path="./not/existing/dir/"
        )
    )
    assert saved_markdown_file_paths == []

    hash_file_path_1: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=_test_module_path,
        hash_type=lint_and_doc_hash_util.HashType.DOCSTRING_TO_MARKDOWN,
    )
    hash_file_path_2: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=init_path,
        hash_type=lint_and_doc_hash_util.HashType.DOCSTRING_TO_MARKDOWN,
    )
    for hash_file_path in (hash_file_path_1, hash_file_path_2):
        file_util.remove_file_if_exists(file_path=hash_file_path)
    saved_markdown_file_paths = docstring_to_markdown_converter.convert_recursively(
        dir_path=_test_module_dir_path
    )
    assert len(saved_markdown_file_paths) == 2
    assert (
        "test_module_1.md" in saved_markdown_file_paths[0]
        or "test_module_1.md" in saved_markdown_file_paths[1]
    )

    saved_markdown_file_paths = docstring_to_markdown_converter.convert_recursively(
        dir_path=_test_module_dir_path
    )
    assert saved_markdown_file_paths == []

    shutil.rmtree("./docstring_markdowns/tmp/", ignore_errors=True)
    for hash_file_path in (hash_file_path_1, hash_file_path_2):
        file_util.remove_file_if_exists(file_path=hash_file_path)


@apply_test_settings()
def test__get_excluding_target_builtin_methods() -> None:
    excluding_target_builtin_methods_dict: Dict[str, str] = (
        docstring_to_markdown_converter._get_excluding_target_builtin_methods()
    )
    assert excluding_target_builtin_methods_dict["__hash__"] == ("Return hash(self).")


@apply_test_settings()
def test__is_excluding_dir_path() -> None:
    result: bool = docstring_to_markdown_converter._is_excluding_dir_path(
        dir_path="./apysc/_translation/jp/sprite.py"
    )
    assert result

    result = docstring_to_markdown_converter._is_excluding_dir_path(
        dir_path="./apysc/_display/sprite.py"
    )
    assert not result
