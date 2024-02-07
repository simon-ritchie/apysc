import inspect
import os
from inspect import Signature
from typing import Callable
from typing import List

from apysc._display import stage
from apysc._file import file_util
from apysc._lint_and_doc import docstring_util
from apysc._lint_and_doc.docstring_util import Example
from apysc._lint_and_doc.docstring_util import Parameter
from apysc._lint_and_doc.docstring_util import Raise
from apysc._lint_and_doc.docstring_util import Reference
from apysc._lint_and_doc.docstring_util import Return
from apysc._lint_and_doc.docstring_util import _DocstringCallableNotExistsError
from apysc._lint_and_doc.docstring_util import _DocstringPathNotFoundError
from apysc._lint_and_doc.docstring_util import _ParamOrRtnBase
from apysc._lint_and_doc.docstring_util import _SectionPattern
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import assert_raises


@apply_test_settings()
def test__get_docstring_path_comment_matches() -> None:
    matches: List[str] = docstring_util._get_docstring_path_comment_matches(
        md_txt=(
            "# Test title"
            "\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->"
            "\n## Sub heading"
            "\n<!-- Docstring:apysc._display.sprite.Sprite.add_child-->"
        )
    )
    assert matches == [
        "<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->",
        "<!-- Docstring:apysc._display.sprite.Sprite.add_child-->",
    ]


@apply_test_settings()
def test__extract_docstring_path_specification_comment_from_line() -> None:
    docstring_path_specification_comment: str = (
        docstring_util._extract_docstring_path_specification_comment_from_line(
            line="<!-- Docstring: apysc._display.sprite.Sprite.add_child -->",
            matches=[
                "<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->",
                "<!-- Docstring: apysc._display.sprite.Sprite.add_child -->",
            ],
        )
    )
    assert (
        docstring_path_specification_comment
        == "<!-- Docstring: apysc._display.sprite.Sprite.add_child -->"
    )

    docstring_path_specification_comment = (
        docstring_util._extract_docstring_path_specification_comment_from_line(
            line="## Test sub heading",
            matches=[
                "<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->",
                "<!-- Docstring: apysc._display.sprite.Sprite.add_child -->",
            ],
        )
    )
    assert docstring_path_specification_comment == ""


@apply_test_settings()
def test__remove_replaced_docstring_section_from_md_txt() -> None:
    md_txt: str = (
        "# Test title"
        "\n\nLorem ipsum dolor sit amet."
        "\n\n## Sub heading 1"
        "\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->"
        "\n\n**Parameters**"
        "\n\n- a: str"
        "\n\n## Sub heading 2"
        "\n\nLorem ipsum dolor sit amet."
        "\n\n## Sub heading 3"
        "\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->"
        "\n\n**Parameters**"
        "\n\n- b: str"
        "\n\n## Sub heading 4"
        "\n\nLorem ipsum dolor sit amet."
    )
    md_txt = docstring_util._remove_replaced_docstring_section_from_md_txt(
        md_txt=md_txt,
        matches=[
            "<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->",
            "<!-- Docstring: apysc._display.sprite.Sprite.add_child -->",
        ],
    )
    expected: str = (
        "# Test title"
        "\n\nLorem ipsum dolor sit amet."
        "\n\n## Sub heading 1"
        "\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->"
        "\n\n## Sub heading 2"
        "\n\nLorem ipsum dolor sit amet."
        "\n\n## Sub heading 3"
        "\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->"
        "\n\n## Sub heading 4"
        "\n\nLorem ipsum dolor sit amet."
    )
    assert md_txt == expected


@apply_test_settings()
def test_reset_replaced_docstring_section() -> None:
    tmp_md_file_path: str = "./tmp/test_docstring_util_1.md"
    os.makedirs("./tmp/", exist_ok=True)
    file_util.remove_file_if_exists(file_path=tmp_md_file_path)

    with open(tmp_md_file_path, "w") as f:
        f.write("# Test title" "\n\nLorem ipsum dolor sit amet.")
    is_executed = docstring_util.reset_replaced_docstring_section(
        md_file_path=tmp_md_file_path
    )
    assert not is_executed

    with open(tmp_md_file_path, "w") as f:
        f.write(
            "# Test title"
            "\n\nLorem ipsum dolor sit amet."
            "\n\n## Sub heading 1"
            "\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->"
            "\n\n**Parameters**"
            "\n\n- a: str"
            "\n\n## Sub heading 2"
            "\n\nLorem ipsum dolor sit amet."
            "\n\n## Sub heading 3"
            "\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->"
            "\n\n**Parameters**"
            "\n\n- b: str"
            "\n\n## Sub heading 4"
            "\n\nLorem ipsum dolor sit amet."
        )
    is_executed = docstring_util.reset_replaced_docstring_section(
        md_file_path=tmp_md_file_path
    )
    assert is_executed
    saved_md_txt: str = file_util.read_txt(file_path=tmp_md_file_path)
    expected: str = (
        "# Test title"
        "\n\nLorem ipsum dolor sit amet."
        "\n\n## Sub heading 1"
        "\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->"
        "\n\n## Sub heading 2"
        "\n\nLorem ipsum dolor sit amet."
        "\n\n## Sub heading 3"
        "\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->"
        "\n\n## Sub heading 4"
        "\n\nLorem ipsum dolor sit amet."
    )
    assert saved_md_txt == expected

    file_util.remove_file_if_exists(file_path=tmp_md_file_path)


@apply_test_settings()
def test__extract_path_from_docstring_comment() -> None:
    path: str = docstring_util._extract_path_from_docstring_comment(
        docstring_path_comment="# Test title"
    )
    assert path == ""

    path = docstring_util._extract_path_from_docstring_comment(
        docstring_path_comment=(
            "<!-- Docstring: apysc._display.sprite.Sprite.add_child -->"
        )
    )
    assert path == "apysc._display.sprite.Sprite.add_child"


@apply_test_settings()
def test__extract_package_path_and_callable_name_from_path() -> None:
    module_or_class_package_path: str
    callable_name: str
    (
        module_or_class_package_path,
        callable_name,
    ) = docstring_util._extract_package_path_and_callable_name_from_path(
        docstring_path_comment="# Test title"
    )
    assert module_or_class_package_path == ""
    assert callable_name == ""

    (
        module_or_class_package_path,
        callable_name,
    ) = docstring_util._extract_package_path_and_callable_name_from_path(
        docstring_path_comment=(
            "<!-- Docstring: apysc._display.sprite.Sprite.add_child -->"
        )
    )
    assert module_or_class_package_path == "apysc._display.sprite.Sprite"
    assert callable_name == "add_child"


@apply_test_settings()
def test__is_section_line() -> None:
    result: bool = docstring_util._is_section_line(line="    Parameters")
    assert result

    result = docstring_util._is_section_line(line="        Parameters")
    assert result

    result = docstring_util._is_section_line(line="    Returns")
    assert result

    result = docstring_util._is_section_line(line="Test function.")
    assert not result


@apply_test_settings()
def test_extract_summary_from_docstring() -> None:
    summary: str = docstring_util.extract_summary_from_docstring(
        docstring=_TEST_DOCSTRING
    )
    assert summary == (
        "Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, sed do eiusmod tempor incididunt "
        "ut labore et dolore magna aliqua."
    )

    docstring: str = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing"
        "\n    elit, sed do eiusmod tempor incididunt ut."
        "\n    Parameters"
        "\n    ----------"
        "\n    a : int"
    )
    summary = docstring_util.extract_summary_from_docstring(docstring=docstring)
    assert summary == (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        "sed do eiusmod tempor incididunt ut."
    )


@apply_test_settings()
def test__is_target_section_pattern_line() -> None:
    result: bool = docstring_util._is_target_section_pattern_line(
        line="    Parameters", section_pattern=_SectionPattern.PARAMETERS
    )
    assert result

    result = docstring_util._is_target_section_pattern_line(
        line="    a : str", section_pattern=_SectionPattern.PARAMETERS
    )
    assert not result

    result = docstring_util._is_target_section_pattern_line(
        line="    Returns", section_pattern=_SectionPattern.PARAMETERS
    )
    assert not result

    result = docstring_util._is_target_section_pattern_line(
        line="    Returns", section_pattern=_SectionPattern.RETURNS
    )
    assert result


@apply_test_settings()
def test__is_hyphens_line() -> None:
    line: str = "    Parameters"
    result: bool = docstring_util._is_hyphens_line(line=line)
    assert not result

    line = "    ----------"
    result = docstring_util._is_hyphens_line(line=line)
    assert result


@apply_test_settings()
def test__get_value_name_and_type_from_line() -> None:
    value_name: str
    type_name: str
    value_name, type_name = docstring_util._get_value_name_and_type_from_line(
        line="    Lorem ipsum dolor sit"
    )
    assert value_name == ""
    assert type_name == ""

    value_name, type_name = docstring_util._get_value_name_and_type_from_line(
        line="    any_value : int"
    )
    assert value_name == "any_value"
    assert type_name == "int"


@apply_test_settings()
def test__get_indent_num_from_line() -> None:
    indent_num: int = docstring_util._get_indent_num_from_line(
        line="    any_value : int"
    )
    assert indent_num == 1

    indent_num = docstring_util._get_indent_num_from_line(
        line="        any_value : int"
    )
    assert indent_num == 2


@apply_test_settings()
def test__remove_line_breaks_and_unnecessary_spaces() -> None:
    text: str = docstring_util._remove_line_breaks_and_unnecessary_spaces(
        text=(
            "    Lorem ipsum dolor sit amet, consectetur   "
            "\nadipiscing elit, sed do eiusmod  tempor incididunt "
            "\nut labore et dolore magna aliqua. "
        )
    )
    assert text == (
        "Lorem ipsum dolor sit amet, consectetur adipiscing "
        "elit, sed do eiusmod tempor incididunt ut labore et "
        "dolore magna aliqua."
    )


_TEST_DOCSTRING: str = (
    "\n    Lorem ipsum dolor sit amet, consectetur "
    "\n    adipiscing elit, sed do eiusmod tempor incididunt "
    "\n    ut labore et dolore magna aliqua."
    "\n"
    "\n    Parameters"
    "\n    ----------"
    "\n    test_param_1 : int"
    "\n        Ut enim ad minim veniam, quis nostrud exercitation"
    "\n        ullamco laboris nisi."
    "\n    test_param_2 : str, optional"
    "\n        Ut aliquip ex ea commodo consequat."
    "\n        Duis aute irure dolor in reprehenderit in"
    "\n        voluptate velit esse cillum dolore."
    "\n"
    "\n        Omnis dolor repellendus. Temporibus autem quibusdam."
    "\n"
    "\n    Returns"
    "\n    -------"
    "\n    test_return_val_1 : bool or int"
    "\n        Fugiat nulla pariatur. Excepteur sint occaecat "
    "\n        cupidatat non proident, sunt in culpa qui "
    "\n        officia deserunt mollit anim id est laborum."
    "\n"
    "\n        Omnis dolor repellendus. Temporibus autem quibusdam."
    "\n    test_return_val_2 : Sprite"
    "\n        Officiis debitis aut rerum necessitatibus saepe eveniet."
    "\n"
    "\n    Notes"
    "\n    -----"
    "\n    At vero eos et accusamus et iusto odio dignissimos"
    "\n    ducimus, qui blanditiis praesentium voluptatum"
    "\n    deleniti atque corrupt."
    "\n"
    "\n    Raises"
    "\n    ------"
    "\n    ValueError"
    "\n        Quos dolores et quas molestias excepturi sint,"
    "\n        obcaecati."
    "\n    ImportError"
    "\n        Cupiditate non provident, similique sunt in culpa."
    "\n"
    "\n    Examples"
    "\n    --------"
    "\n    >>> test_value_1: int = 10"
    "\n    >>> test_value_1"
    "\n    10"
    "\n"
    "\n    >>> test_value_2: int = test_function("
    "\n    ...    any_arg=10)"
    "\n    >>> test_value_2"
    "\n    30"
    "\n"
    "\n    >>> test_value_3: int = x + 10"
    "\n"
    "\n    References"
    "\n    ----------"
    "\n    - Test interface1 document"
    "\n        - https://en.wikipedia.org/test_page_1.html"
    "\n    - Test interface2 document"
    "\n        - https://en.wikipedia.org/test_page_2.html"
)


@apply_test_settings()
def test_extract_param_or_rtn_values_from_docstring() -> None:
    param_values: List[Parameter] = (
        docstring_util.extract_param_or_rtn_values_from_docstring(
            target_type=Parameter, docstring=_TEST_DOCSTRING
        )
    )
    assert len(param_values) == 2
    for parameter_ in param_values:
        assert isinstance(parameter_, Parameter)
    parameter: Parameter = Parameter(
        name="test_param_1",
        type_str="int",
        description=(
            "Ut enim ad minim veniam, quis nostrud exercitation "
            "ullamco laboris nisi."
        ),
    )
    assert param_values[0] == parameter
    parameter = Parameter(
        name="test_param_2",
        type_str="str, optional",
        description=(
            "Ut aliquip ex ea commodo consequat. "
            "Duis aute irure dolor in reprehenderit in "
            "voluptate velit esse cillum dolore. "
            "Omnis dolor repellendus. Temporibus autem quibusdam."
        ),
    )
    assert param_values[1] == parameter

    return_values: List[Return] = (
        docstring_util.extract_param_or_rtn_values_from_docstring(
            target_type=Return, docstring=_TEST_DOCSTRING
        )
    )
    assert len(return_values) == 2
    for return__ in return_values:
        assert isinstance(return__, Return)
    return_: Return = Return(
        name="test_return_val_1",
        type_str="bool or int",
        description=(
            "Fugiat nulla pariatur. Excepteur sint occaecat "
            "cupidatat non proident, sunt in culpa qui "
            "officia deserunt mollit anim id est laborum. "
            "Omnis dolor repellendus. Temporibus autem quibusdam."
        ),
    )
    assert return_values[0] == return_
    return_ = Return(
        name="test_return_val_2",
        type_str="Sprite",
        description=("Officiis debitis aut rerum necessitatibus saepe eveniet."),
    )


@apply_test_settings()
def test__make_prm_or_rtn_description_and_append_to_list() -> None:
    parameters: List[Parameter] = []

    docstring_util._make_prm_or_rtn_description_and_append_to_list(
        target_type=Parameter,
        param_or_rtn_values=parameters,
        value_name="test_value",
        value_type_str="int",
        description_lines=[],
    )
    assert parameters == []

    description_lines: List[str] = [
        "    At vero eos et accusamus et iusto odio dignissimos"
        "    ducimus, qui blanditiis praesentium voluptatum."
    ]
    docstring_util._make_prm_or_rtn_description_and_append_to_list(
        target_type=Parameter,
        param_or_rtn_values=parameters,
        value_name="test_value",
        value_type_str="int",
        description_lines=description_lines,
    )
    parameter: Parameter = Parameter(
        name="test_value",
        type_str="int",
        description=(
            "At vero eos et accusamus et iusto odio dignissimos "
            "ducimus, qui blanditiis praesentium voluptatum."
        ),
    )
    assert parameters == [parameter]
    assert isinstance(parameters[0], Parameter)
    assert description_lines == []


class Test_ParamOrRtnBase:
    @apply_test_settings()
    def test___init__(self) -> None:
        param_or_rtn: _ParamOrRtnBase = _ParamOrRtnBase(
            name="test_value", type_str="int", description="Lorem ipsum dolor sit."
        )
        assert_attrs(
            expected_attrs={
                "_name": "test_value",
                "_type_str": "int",
                "_description": "Lorem ipsum dolor sit.",
            },
            any_obj=param_or_rtn,
        )

    @apply_test_settings()
    def test___eq__(self) -> None:
        param_or_rtn: _ParamOrRtnBase = _ParamOrRtnBase(
            name="test_value", type_str="int", description="Lorem ipsum dolor sit."
        )
        result: bool = param_or_rtn == 10
        assert not result

        other: _ParamOrRtnBase = _ParamOrRtnBase(
            name="test_value_2", type_str="int", description="Lorem ipsum dolor sit."
        )
        result = param_or_rtn == other
        assert not result

        other = _ParamOrRtnBase(
            name="test_value", type_str="str", description="Lorem ipsum dolor sit."
        )
        result = param_or_rtn == other
        assert not result

        other = _ParamOrRtnBase(
            name="test_value", type_str="int", description="Lorem ipsum dolor."
        )
        result = param_or_rtn == other
        assert not result

        other = _ParamOrRtnBase(
            name="test_value", type_str="int", description="Lorem ipsum dolor sit."
        )
        result = param_or_rtn == other
        assert result

    @apply_test_settings()
    def test_name(self) -> None:
        param_or_rtn: _ParamOrRtnBase = _ParamOrRtnBase(
            name="test_value", type_str="int", description="Lorem ipsum dolor sit."
        )
        assert param_or_rtn.name == "test_value"

    @apply_test_settings()
    def test_type_str(self) -> None:
        param_or_rtn: _ParamOrRtnBase = _ParamOrRtnBase(
            name="test_value", type_str="int", description="Lorem ipsum dolor sit."
        )
        assert param_or_rtn.type_str == "int"

    @apply_test_settings()
    def test_description(self) -> None:
        param_or_rtn: _ParamOrRtnBase = _ParamOrRtnBase(
            name="test_value", type_str="int", description="Lorem ipsum dolor sit."
        )
        assert param_or_rtn.description == "Lorem ipsum dolor sit."


@apply_test_settings()
def test__get_params_or_rtns_section_pattern_by_type() -> None:
    pattern: _SectionPattern = (
        docstring_util._get_params_or_rtns_section_pattern_by_type(
            target_type=Parameter
        )
    )
    assert pattern == _SectionPattern.PARAMETERS

    pattern = docstring_util._get_params_or_rtns_section_pattern_by_type(
        target_type=Return
    )
    assert pattern == _SectionPattern.RETURNS

    assert_raises(
        expected_error_class=ValueError,
        callable_=docstring_util._get_params_or_rtns_section_pattern_by_type,
        match="Invalid type argument is provided: ",
        target_type=10,
    )


class Test_Raise:
    @apply_test_settings()
    def test___init__(self) -> None:
        raise_: Raise = Raise(
            err_class_name="ValueError", description="Lorem ipsum dolor sit."
        )
        assert_attrs(
            expected_attrs={
                "_err_class_name": "ValueError",
                "_description": "Lorem ipsum dolor sit.",
            },
            any_obj=raise_,
        )

    @apply_test_settings()
    def test_err_class_name(self) -> None:
        raise_: Raise = Raise(
            err_class_name="ValueError", description="Lorem ipsum dolor sit."
        )
        assert raise_.err_class_name == "ValueError"

    @apply_test_settings()
    def test_description(self) -> None:
        raise_: Raise = Raise(
            err_class_name="ValueError", description="Lorem ipsum dolor sit."
        )
        assert raise_.description == "Lorem ipsum dolor sit."

    @apply_test_settings()
    def test___eq__(self) -> None:
        raise_: Raise = Raise(
            err_class_name="ValueError", description="Lorem ipsum dolor sit."
        )

        result: bool = raise_ == 10
        assert not result

        other: Raise = Raise(
            err_class_name="ImportError", description="Lorem ipsum dolor sit."
        )
        result = raise_ == other
        assert not result

        other = Raise(err_class_name="ValueError", description="Lorem ipsum dolor.")
        result = raise_ == other
        assert not result

        other = Raise(err_class_name="ValueError", description="Lorem ipsum dolor sit.")
        result = raise_ == other
        assert result


@apply_test_settings()
def test__make_raise_description_and_append_to_list() -> None:
    raise_values: List[Raise] = []

    docstring_util._make_raise_description_and_append_to_list(
        raise_values=raise_values, err_class_name="ValueError", description_lines=[]
    )
    assert raise_values == []

    docstring_util._make_raise_description_and_append_to_list(
        raise_values=raise_values,
        err_class_name="ValueError",
        description_lines=[
            "    Lorem ipsum dolor sit amet, consectetur adipiscing ",
            "    elit, sed do eiusmod tempor incididunt ut labore ",
            "    et dolore magna aliqua. ",
        ],
    )
    expected_raise: Raise = Raise(
        err_class_name="ValueError",
        description=(
            "Lorem ipsum dolor sit amet, consectetur adipiscing "
            "elit, sed do eiusmod tempor incididunt ut labore "
            "et dolore magna aliqua."
        ),
    )
    assert raise_values == [expected_raise]


@apply_test_settings()
def test_extract_raise_values_from_docstring() -> None:
    raise_values: List[Raise] = docstring_util.extract_raise_values_from_docstring(
        docstring=_TEST_DOCSTRING
    )
    assert len(raise_values) == 2
    expected_raise: Raise = Raise(
        err_class_name="ValueError",
        description=("Quos dolores et quas molestias excepturi sint, " "obcaecati."),
    )
    assert raise_values[0] == expected_raise

    expected_raise = Raise(
        err_class_name="ImportError",
        description=("Cupiditate non provident, similique sunt in culpa."),
    )
    assert raise_values[1] == expected_raise


@apply_test_settings()
def test__get_base_indent_num_if_not_set() -> None:
    base_indent_num: int = docstring_util._get_base_indent_num_if_not_set(
        line="        test_value : int", base_indent_num=1
    )
    assert base_indent_num == 1

    base_indent_num = docstring_util._get_base_indent_num_if_not_set(
        line="    Lorem ipsum dolor sit.", base_indent_num=0
    )
    assert base_indent_num == 1


@apply_test_settings()
def test__remove_blank_lines_from_list() -> None:
    result_lines: List[str] = docstring_util._remove_blank_lines_from_list(
        lines=[
            "    Lorem ipsum dolor sit amet, consectetur adipiscing",
            "",
            "    ",
            "    elit, sed do eiusmod tempor incididunt ut.",
        ]
    )
    assert result_lines == [
        "    Lorem ipsum dolor sit amet, consectetur adipiscing",
        "    elit, sed do eiusmod tempor incididunt ut.",
    ]


@apply_test_settings()
def test__is_skip_target_line() -> None:
    result: bool = docstring_util._is_skip_target_line(
        is_target_section_range=False, line="        any_value : int"
    )
    assert result

    result = docstring_util._is_skip_target_line(
        is_target_section_range=True, line="    ------"
    )
    assert result

    result = docstring_util._is_skip_target_line(
        is_target_section_range=True, line="        any_value : int"
    )
    assert not result


@apply_test_settings()
def test_extract_notes_from_docstring() -> None:
    notes: str = docstring_util.extract_notes_from_docstring(docstring=_TEST_DOCSTRING)
    assert notes == (
        "At vero eos et accusamus et iusto odio dignissimos "
        "ducimus, qui blanditiis praesentium voluptatum "
        "deleniti atque corrupt."
    )


class Test_Reference:
    @apply_test_settings()
    def test___init__(self) -> None:
        reference: Reference = Reference(
            page_label="Sprite document",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        )
        assert_attrs(
            expected_attrs={
                "_page_label": "Sprite document",
                "_url": "https://simon-ritchie.github.io/apysc/sprite.html",
            },
            any_obj=reference,
        )

    @apply_test_settings()
    def test_page_label(self) -> None:
        reference: Reference = Reference(
            page_label="Sprite document",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        )
        assert reference.page_label == "Sprite document"

    @apply_test_settings()
    def test_url(self) -> None:
        reference: Reference = Reference(
            page_label="Sprite document",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        )
        assert reference.url == "https://simon-ritchie.github.io/apysc/sprite.html"

    @apply_test_settings()
    def test___eq__(self) -> None:
        reference: Reference = Reference(
            page_label="Sprite document",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        )
        result: bool = reference == 10
        assert not result

        other: Reference = Reference(
            page_label="DisplayObject document",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        )
        result = reference == other
        assert not result

        other = Reference(
            page_label="Sprite document",
            url="https://simon-ritchie.github.io/apysc/display_object.html",
        )
        result = reference == other
        assert not result

        other = Reference(
            page_label="Sprite document",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        )
        result = reference == other
        assert result


@apply_test_settings()
def test__remove_unnecessary_markdown_list_from_line() -> None:
    line: str = docstring_util._remove_unnecessary_markdown_list_from_line(
        line="    - Sprite document"
    )
    assert line == "Sprite document"


@apply_test_settings()
def test__make_reference_and_append_to_list() -> None:
    reference_values: List[Reference] = []

    docstring_util._make_reference_and_append_to_list(
        reference_values=reference_values, page_label="Sprite document", url=""
    )
    assert reference_values == []

    docstring_util._make_reference_and_append_to_list(
        reference_values=reference_values,
        page_label="Sprite document",
        url="https://simon-ritchie.github.io/apysc/sprite.html",
    )
    expected_reference: Reference = Reference(
        page_label="Sprite document",
        url="https://simon-ritchie.github.io/apysc/sprite.html",
    )
    assert reference_values == [expected_reference]


@apply_test_settings()
def test_extract_reference_values_from_docstring() -> None:
    reference_values: List[Reference] = (
        docstring_util.extract_reference_values_from_docstring(
            docstring=_TEST_DOCSTRING
        )
    )
    assert len(reference_values) == 2
    expected_reference: Reference = Reference(
        page_label="Test interface1 document",
        url="https://en.wikipedia.org/test_page_1.html",
    )
    assert reference_values[0] == expected_reference

    expected_reference = Reference(
        page_label="Test interface2 document",
        url="https://en.wikipedia.org/test_page_2.html",
    )
    assert reference_values[1] == expected_reference


@apply_test_settings()
def test_append_params_or_rtns_to_markdown() -> None:
    markdown: str = "## add_child interface api document"
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=[]
    )
    assert markdown == "## add_child interface api document"

    parameters: List[Parameter] = [
        Parameter(
            name="test_param_1", type_str="int", description="Lorem ipsum dolor sit."
        ),
        Parameter(
            name="test_param_2",
            type_str="str, optional",
            description="Amet, consectetur adipiscing elit.",
        ),
    ]
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=parameters
    )
    expected: str = (
        "## add_child interface api document"
        "\n\n**[Parameters]**"
        "\n\n- `test_param_1`: int"
        "\n  - Lorem ipsum dolor sit."
        "\n- `test_param_2`: str, optional"
        "\n  - Amet, consectetur adipiscing elit."
        "\n\n<hr>"
    )
    assert markdown == expected

    returns: List[Return] = [
        Return(
            name="test_return_value",
            type_str="int",
            description="Lorem  ipsum dolor sit.",
        ),
    ]
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=returns
    )
    expected = (
        "## add_child interface api document"
        "\n\n**[Parameters]**"
        "\n\n- `test_param_1`: int"
        "\n  - Lorem ipsum dolor sit."
        "\n- `test_param_2`: str, optional"
        "\n  - Amet, consectetur adipiscing elit."
        "\n\n<hr>"
        "\n\n**[Returns]**"
        "\n\n- `test_return_value`: int"
        "\n  - Lorem  ipsum dolor sit."
        "\n\n<hr>"
    )
    assert markdown == expected


@apply_test_settings()
def test_append_raises_to_markdown() -> None:
    markdown: str = "## add_child interface api document"
    markdown = docstring_util.append_raises_to_markdown(markdown=markdown, raises=[])
    assert markdown == "## add_child interface api document"

    raises: List[Raise] = [
        Raise(err_class_name="ValueError", description="Lorem ipsum dolor sit."),
        Raise(
            err_class_name="ImportError",
            description="Amet, consectetur adipiscing elit.",
        ),
    ]
    markdown = docstring_util.append_raises_to_markdown(
        markdown=markdown, raises=raises
    )
    expected: str = (
        "## add_child interface api document"
        "\n\n**[Raises]**"
        "\n\n- ValueError: Lorem ipsum dolor sit."
        "\n- ImportError: Amet, consectetur adipiscing elit."
        "\n\n<hr>"
    )
    assert markdown == expected


@apply_test_settings()
def test_append_notes_to_markdown() -> None:
    markdown: str = "## add_child interface api document"
    markdown = docstring_util.append_notes_to_markdown(markdown=markdown, notes="")
    assert markdown == "## add_child interface api document"

    markdown = docstring_util.append_notes_to_markdown(
        markdown=markdown, notes="Lorem ipsum dolor sit."
    )
    assert markdown == (
        "## add_child interface api document"
        "\n\n**[Notes]**"
        "\n\nLorem ipsum dolor sit.<hr>"
    )

    markdown = "## add_child interface api document"
    markdown = docstring_util.append_notes_to_markdown(
        markdown=markdown, notes="<br>・Lorem ipsum.<br>・dolor sit."
    )
    assert markdown == (
        "## add_child interface api document"
        "\n\n**[Notes]**"
        "\n\n・Lorem ipsum."
        "<br>・dolor sit.<hr>"
    )


@apply_test_settings()
def test_append_references_to_markdown() -> None:
    markdown: str = "## add_child interface api document"
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=[]
    )
    assert markdown == "## add_child interface api document"

    references: List[Reference] = [
        Reference(
            page_label="Sprite document",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        ),
        Reference(
            page_label="DisplayObject document",
            url="https://simon-ritchie.github.io/apysc/display_object.html",
        ),
    ]
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=references
    )
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=[]
    )
    expected: str = (
        "## add_child interface api document"
        "\n\n**[References]**"
        "\n\n- [Sprite document]"
        "(https://simon-ritchie.github.io/apysc/sprite.html)"
        "\n- [DisplayObject document]"
        "(https://simon-ritchie.github.io/apysc/display_object.html)"
        "\n\n<hr>"
    )
    assert markdown == expected


@apply_test_settings()
def test_append_summary_to_markdown() -> None:
    markdown: str = "## add_child interface api document"
    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown, summary="", heading_label="**[Interface summary]** "
    )
    assert markdown == "## add_child interface api document"

    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown,
        summary="Lorem ipsum dolor sit.",
        heading_label="**[Interface summary]** ",
    )
    assert markdown == (
        "## add_child interface api document"
        "\n\n**[Interface summary]** "
        "Lorem ipsum dolor sit.<hr>"
    )

    markdown = "## add_child interface api document"
    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown,
        summary="<br>・Lorem ipsum.<br>・dolor sit.",
        heading_label="**[Interface summary]** ",
    )
    assert markdown == (
        "## add_child interface api document"
        "\n\n**[Interface summary]** "
        "・Lorem ipsum.<br>・dolor sit.<hr>"
    )


@apply_test_settings()
def test__convert_docstring_to_markdown() -> None:
    signature: Signature = inspect.signature(test__convert_docstring_to_markdown)
    markdown: str = docstring_util._convert_docstring_to_markdown(
        docstring=_TEST_DOCSTRING,
        signature=signature,
        callable_name="test_func",
        md_file_path="./docs_src/source/test_document.md",
    )
    markdown_lines: List[str] = markdown.splitlines()
    expected_lines: List[str] = [
        '<span class="inconspicuous-txt">Note: the document '
        "build script generates and updates this "
        "API document section automatically. Maybe this section "
        "is duplicated compared with previous sections.</span>",
        "",
        "**[Interface signature]** " "`test_func() -> None`<hr>",
        "",
        "**[Interface summary]**",
        "",
        "Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, sed do eiusmod tempor incididunt "
        "ut labore et dolore magna aliqua.<hr>",
        "",
        "**[Parameters]**",
        "",
        "- `test_param_1`: int",
        "  - Ut enim ad minim veniam, quis nostrud exercitation "
        "ullamco laboris nisi.",
        "- `test_param_2`: str, optional",
        "  - Ut aliquip ex ea commodo consequat. "
        "Duis aute irure dolor in reprehenderit in "
        "voluptate velit esse cillum dolore. "
        "Omnis dolor repellendus. Temporibus autem quibusdam.",
        "",
        "<hr>",
        "",
        "**[Returns]**",
        "",
        "- `test_return_val_1`: bool or int",
        "  - Fugiat nulla pariatur. Excepteur sint occaecat "
        "cupidatat non proident, sunt in culpa qui "
        "officia deserunt mollit anim id est laborum. "
        "Omnis dolor repellendus. Temporibus autem quibusdam.",
        "- `test_return_val_2`: Sprite",
        "  - Officiis debitis aut rerum necessitatibus saepe eveniet.",
        "",
        "<hr>",
        "",
        "**[Raises]**",
        "",
        "- ValueError: Quos dolores et quas molestias excepturi sint, " "obcaecati.",
        "- ImportError: Cupiditate non provident, similique sunt in culpa.",
        "",
        "<hr>",
        "",
        "**[Notes]**",
        "",
        "At vero eos et accusamus et iusto odio dignissimos "
        "ducimus, qui blanditiis praesentium voluptatum "
        "deleniti atque corrupt.<hr>",
        "",
        "**[Examples]**",
        "",
        "```py",
        ">>> test_value_1: int = 10",
        ">>> test_value_1",
        "10",
        "",
        ">>> test_value_2: int = test_function(",
        "...    any_arg=10)",
        ">>> test_value_2",
        "30",
        "",
        ">>> test_value_3: int = x + 10",
        "```",
        "",
        "<hr>",
        "",
        "**[References]**",
        "",
        "- [Test interface1 document]" "(https://en.wikipedia.org/test_page_1.html)",
        "- [Test interface2 document]" "(https://en.wikipedia.org/test_page_2.html)",
    ]
    for i, expected_line in enumerate(expected_lines):
        assert markdown_lines[i] == expected_line
    assert len(markdown_lines) == len(expected_lines)


_PATH_COMMENT_KEYWORD: str = docstring_util.DOCSTRING_PATH_COMMENT_KEYWORD


@apply_test_settings()
def test__convert_docstring_path_comment_to_markdown_format() -> None:
    markdown_format_docstring: str = (
        docstring_util._convert_docstring_path_comment_to_markdown_format(
            docstring_path_comment=(
                f"<!-- {_PATH_COMMENT_KEYWORD}"
                " tests._lint_and_doc.test_docstring_util."
                "test__convert_docstring_path_comment_to_markdown_format"
                " -->"
            ),
            md_file_path="./docs_src/source/test_document.md",
        )
    )
    assert markdown_format_docstring == ""

    markdown_format_docstring = (
        docstring_util._convert_docstring_path_comment_to_markdown_format(
            docstring_path_comment=(
                f"<!-- {_PATH_COMMENT_KEYWORD} "
                "apysc._display.sprite.Sprite.__init__ -->"
            ),
            md_file_path="./docs_src/source/test_document.md",
        )
    )
    assert "**[Interface summary]**" in markdown_format_docstring
    assert (
        "Create a basic display object that can be a parent."
        in markdown_format_docstring
    )


@apply_test_settings()
def test_replace_docstring_path_specification() -> None:
    tmp_dir_path: str = "./tmp/"
    os.makedirs(tmp_dir_path, exist_ok=True)
    tmp_md_path: str = os.path.join(tmp_dir_path, "tmp_md_path.md")
    with open(tmp_md_path, "w") as f:
        f.write(
            "# Test document"
            "\n\nLorem ipsum dolor sit amet."
            "\n\n## Constructor interface API"
            f"\n\n<!-- {_PATH_COMMENT_KEYWORD} "
            "apysc._display.sprite.Sprite.__init__ -->"
        )
    file_util.save_plain_txt(
        txt=(
            "# Test document"
            "\n\nLorem ipsum dolor sit amet."
            "\n\n## Constructor API"
            f"\n\n<!-- {_PATH_COMMENT_KEYWORD} "
            "apysc._display.sprite.Sprite.__init__ -->"
        ),
        file_path=tmp_md_path,
    )
    docstring_util.replace_docstring_path_specification(md_file_path=tmp_md_path)
    md_txt: str = file_util.read_txt(file_path=tmp_md_path)
    assert md_txt.startswith("# Test document")
    assert (
        f"\n\n<!-- {_PATH_COMMENT_KEYWORD} " "apysc._display.sprite.Sprite.__init__ -->"
    ) in md_txt
    assert "**[Interface summary]**" in md_txt

    file_util.remove_file_if_exists(file_path=tmp_md_path)


@apply_test_settings()
def test__get_callable_from_package_path_and_callable_name() -> None:
    assert_raises(
        expected_error_class=_DocstringPathNotFoundError,
        callable_=docstring_util._get_callable_from_package_path_and_callable_name,
        match="Module or class package path: not.existing.package.path",
        module_or_class_package_path="not.existing.package.path",
        callable_name="__init__",
    )

    assert_raises(
        expected_error_class=_DocstringCallableNotExistsError,
        callable_=docstring_util._get_callable_from_package_path_and_callable_name,
        match="Callable name: not_existing_method",
        module_or_class_package_path="apysc._display.sprite.Sprite",
        callable_name="not_existing_method",
    )

    callable_: Callable = (
        docstring_util._get_callable_from_package_path_and_callable_name(
            module_or_class_package_path="apysc._display.sprite.Sprite",
            callable_name="__init__",
        )
    )
    assert callable_.__name__ == "__init__"


class Test_Example:
    @apply_test_settings()
    def test___init__(self) -> None:
        example: Example = Example(input_code_block="x = 10\nx", expected_output="10")
        assert_attrs(
            expected_attrs={
                "_input_code_block": "x = 10\nx",
                "_expected_output": "10",
            },
            any_obj=example,
        )

    @apply_test_settings()
    def test_input_code_block(self) -> None:
        example: Example = Example(input_code_block="x = 10\nx", expected_output="10")
        assert example.input_code_block == "x = 10\nx"

    @apply_test_settings()
    def test_expected_output(self) -> None:
        example: Example = Example(input_code_block="x = 10\nx", expected_output="10")
        assert example.expected_output == "10"

    @apply_test_settings()
    def test___eq__(self) -> None:
        example: Example = Example(input_code_block="x = 10\nx", expected_output="10")

        result: bool = example == 10
        assert not result

        other: Example = Example(input_code_block="x = 10", expected_output="10")
        result = example == other
        assert not result

        other = Example(input_code_block="x = 10\nx", expected_output="20")
        result = example == other
        assert not result

        other = Example(input_code_block="x = 10\nx", expected_output="10")
        result = example == other
        assert result


@apply_test_settings()
def test__is_example_output_line() -> None:
    result: bool = docstring_util._is_example_output_line(line="    >>> x = 10")
    assert not result

    result = docstring_util._is_example_output_line(line="    ...     x=10,")
    assert not result

    result = docstring_util._is_example_output_line(line="    10")
    assert result


@apply_test_settings()
def test__make_example_and_append_to_list() -> None:
    example_values: List[Example] = []
    docstring_util._make_example_and_append_to_list(
        example_values=example_values,
        input_code_block_lines=[],
        expected_output="    10",
    )
    assert example_values == []

    input_code_block_lines: List[str] = [
        "    >>> x = 10",
        "    >>> x",
    ]
    docstring_util._make_example_and_append_to_list(
        example_values=example_values,
        input_code_block_lines=input_code_block_lines,
        expected_output="    10",
    )
    assert input_code_block_lines == []
    assert example_values == [
        Example(input_code_block=">>> x = 10\n>>> x", expected_output="10")
    ]


@apply_test_settings()
def test_extract_example_values_from_docstring() -> None:
    example_values: List[Example] = (
        docstring_util.extract_example_values_from_docstring(docstring=_TEST_DOCSTRING)
    )
    assert len(example_values) == 3
    assert example_values[0] == Example(
        input_code_block=(">>> test_value_1: int = 10" "\n>>> test_value_1"),
        expected_output="10",
    )

    assert example_values[1] == Example(
        input_code_block=(
            ">>> test_value_2: int = test_function("
            "\n...    any_arg=10)"
            "\n>>> test_value_2"
        ),
        expected_output="30",
    )

    assert example_values[2] == Example(
        input_code_block=(">>> test_value_3: int = x + 10"), expected_output=""
    )


@apply_test_settings()
def test_append_examples_to_markdown() -> None:
    markdown: str = "## add_child interface api document"
    markdown = docstring_util.append_examples_to_markdown(
        markdown=markdown, examples=[]
    )
    assert markdown == "## add_child interface api document"

    examples: List[Example] = [
        Example(input_code_block=(">>> x = 10" "\n>>> x"), expected_output="10"),
        Example(input_code_block=(">>> y = x + 10"), expected_output=""),
    ]
    markdown = docstring_util.append_examples_to_markdown(
        markdown=markdown, examples=examples
    )
    expected_lines: List[str] = [
        "## add_child interface api document",
        "",
        "**[Examples]**",
        "",
        "```py",
        ">>> x = 10",
        ">>> x",
        "10",
        "",
        ">>> y = x + 10",
        "```",
        "",
        "<hr>",
    ]
    lines: List[str] = markdown.splitlines()
    for i, line in enumerate(lines):
        assert line == expected_lines[i]
    assert len(lines) == len(expected_lines)


@apply_test_settings()
def test__slice_references_by_md_file_path() -> None:
    references: List[Reference] = [
        Reference(
            page_label="test document 1",
            url="https://simon-ritchie.github.io/apysc/sprite.html",
        ),
        Reference(
            page_label="test document 1",
            url="https://simon-ritchie.github.io/apysc/display_object.html",
        ),
    ]
    sliced_references: List[Reference] = (
        docstring_util._slice_references_by_md_file_path(
            references=references, md_file_path="./docs_src/source/sprite.md"
        )
    )
    assert sliced_references == [
        Reference(
            page_label="test document 1",
            url="https://simon-ritchie.github.io/apysc/display_object.html",
        )
    ]


@apply_test_settings()
def test_get_docstring_src_module_paths() -> None:
    module_paths: List[str] = docstring_util.get_docstring_src_module_paths(
        md_file_path="./docs_src/source/int_and_number.md"
    )
    assert "./apysc/_type/int.py" in module_paths
    assert "./apysc/_type/number.py" in module_paths


@apply_test_settings()
def test_remove_trailing_hr_tag() -> None:
    markdown: str = docstring_util.remove_trailing_hr_tag(
        markdown="Lorem ipsum dolor sit.\n\n<hr>\n"
    )
    assert markdown == "Lorem ipsum dolor sit."


@apply_test_settings()
def test__remove_noqa() -> None:
    string: str = docstring_util._remove_noqa(string="Lorem ipsum dolor sit.  # noqa")
    assert string == "Lorem ipsum dolor sit."


@apply_test_settings()
def test__append_br_tag_and_replace_symbol_if_first_char_is_hyphen() -> None:
    line: str = (
        docstring_util._append_br_tag_and_replace_symbol_if_first_char_is_hyphen(
            line="    - Lorem ipsum dolor sit."
        )
    )
    assert line == "<br>    ・Lorem ipsum dolor sit."


@apply_test_settings()
def test_extract_docstrings_from_module() -> None:
    docstrings: List[str] = docstring_util.extract_docstrings_from_module(module=stage)
    expected_keywords: List[str] = [
        "Stage-related implementations.",
        "The Stage (overall view-area) class.",
        "Get an already instantiated stage instance.",
    ]
    for expected_keyword in expected_keywords:
        expected_keyword_exists: bool = False
        for docstring in docstrings:
            if expected_keyword in docstring:
                expected_keyword_exists = True
                break
        assert expected_keyword_exists, expected_keyword
