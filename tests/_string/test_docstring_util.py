import os
from random import randint
from typing import Any, List

from retrying import retry

from apysc._string import docstring_util
from apysc._string.docstring_util import _Parameter, _ParamOrRtnBase, _ParamsOrRtnsSectionPattern, _Return
from apysc._file import file_util
from apysc._display.sprite import Sprite
from apysc._display import sprite
from tests.testing_helper import assert_attrs, assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_docstring_path_comment_matches() -> None:
    matches: List[str] = docstring_util._get_docstring_path_comment_matches(
        md_txt=(
            '# Test title'
            '\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
            '\n## Sub heading'
            '\n<!-- Docstring:apysc._display.sprite.Sprite.add_child-->'
        ))
    assert matches == [
        '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
        '<!-- Docstring:apysc._display.sprite.Sprite.add_child-->',
    ]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_docstring_path_specification_comment_from_line() -> None:
    docstring_path_specification_comment: str = docstring_util.\
        _extract_docstring_path_specification_comment_from_line(
            line='<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            matches=[
                '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            ])
    assert (
        docstring_path_specification_comment ==
        '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->')

    docstring_path_specification_comment = docstring_util.\
        _extract_docstring_path_specification_comment_from_line(
            line='## Test sub heading',
            matches=[
                '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            ])
    assert docstring_path_specification_comment == ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_replaced_docstring_section_from_md_txt() -> None:
    md_txt: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n**Parameters**'
        '\n\n- a: str'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n**Parameters**'
        '\n\n- b: str'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    md_txt = docstring_util._remove_replaced_docstring_section_from_md_txt(
        md_txt=md_txt,
        matches=[
            '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
            '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
        ])
    expected: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    assert md_txt == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_reset_replaced_docstring_section() -> None:
    tmp_md_file_path: str = './tmp/test_docstring_util_1.md'
    os.makedirs('./tmp/', exist_ok=True)
    file_util.remove_file_if_exists(file_path=tmp_md_file_path)

    with open(tmp_md_file_path, 'w') as f:
        f.write(
            '# Test title'
            '\n\nLorem ipsum dolor sit amet.'
        )
    is_executed = docstring_util.reset_replaced_docstring_section(
        md_file_path=tmp_md_file_path)
    assert not is_executed

    with open(tmp_md_file_path, 'w') as f:
        f.write(
            '# Test title'
            '\n\nLorem ipsum dolor sit amet.'
            '\n\n## Sub heading 1'
            '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
            '\n\n**Parameters**'
            '\n\n- a: str'
            '\n\n## Sub heading 2'
            '\n\nLorem ipsum dolor sit amet.'
            '\n\n## Sub heading 3'
            '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
            '\n\n**Parameters**'
            '\n\n- b: str'
            '\n\n## Sub heading 4'
            '\n\nLorem ipsum dolor sit amet.'
        )
    is_executed = docstring_util.reset_replaced_docstring_section(
        md_file_path=tmp_md_file_path)
    assert is_executed
    saved_md_txt: str = file_util.read_txt(file_path=tmp_md_file_path)
    expected: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    assert saved_md_txt == expected

    file_util.remove_file_if_exists(file_path=tmp_md_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_path_from_docstring_comment() -> None:
    path: str = docstring_util._extract_path_from_docstring_comment(
        docstring_path_comment='# Test title')
    assert path == ''

    path = docstring_util._extract_path_from_docstring_comment(
        docstring_path_comment=(
            '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'))
    assert path == 'apysc._display.sprite.Sprite.add_child'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_package_path_and_callable_name_from_path() -> None:
    module_or_class_package_path: str
    callable_name: str
    module_or_class_package_path, callable_name = \
        docstring_util._extract_package_path_and_callable_name_from_path(
            docstring_path_comment='# Test title')
    assert module_or_class_package_path == ''
    assert callable_name == ''

    module_or_class_package_path, callable_name = \
        docstring_util._extract_package_path_and_callable_name_from_path(
            docstring_path_comment=(
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'))
    assert module_or_class_package_path == 'apysc._display.sprite.Sprite'
    assert callable_name == 'add_child'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_section_line() -> None:
    result: bool = docstring_util._is_section_line(
        line='    Parameters')
    assert result

    result = docstring_util._is_section_line(
        line='        Parameters')
    assert result

    result = docstring_util._is_section_line(
        line='    Returns')
    assert result

    result = docstring_util._is_section_line(
        line='Test function.')
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_summary_from_docstring() -> None:
    docstring: str = (
        '    Lorem ipsum dolor sit amet, consectetur adipiscing'
        '\n    elit, sed do eiusmod tempor incididunt ut.'
        '\n    Parameters'
        '\n    ----------'
        '\n    a : int'
    )
    summary: str = docstring_util._extract_summary_from_docstring(
        docstring=docstring)
    assert summary == (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
        'sed do eiusmod tempor incididunt ut.'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_target_section_pattern_line() -> None:
    result: bool = docstring_util._is_target_section_pattern_line(
        line='    Parameters',
        section_pattern=_ParamsOrRtnsSectionPattern.PARAMETERS)
    assert result

    result = docstring_util._is_target_section_pattern_line(
        line='    a : str',
        section_pattern=_ParamsOrRtnsSectionPattern.PARAMETERS)
    assert not result

    result = docstring_util._is_target_section_pattern_line(
        line='    Returns',
        section_pattern=_ParamsOrRtnsSectionPattern.PARAMETERS)
    assert not result

    result = docstring_util._is_target_section_pattern_line(
        line='    Returns',
        section_pattern=_ParamsOrRtnsSectionPattern.RETURNS)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_hyphens_line() -> None:
    line: str = '    Parameters'
    result: bool = docstring_util._is_hyphens_line(line=line)
    assert not result

    line = '    ----------'
    result = docstring_util._is_hyphens_line(line=line)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_value_name_and_type_from_line() -> None:
    value_name: str
    type_name: str
    value_name, type_name = docstring_util._get_value_name_and_type_from_line(
        line='    Lorem ipsum dolor sit')
    assert value_name == ''
    assert type_name == ''

    value_name, type_name = docstring_util._get_value_name_and_type_from_line(
        line='    any_value : int')
    assert value_name == 'any_value'
    assert type_name == 'int'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_indent_num_from_line() -> None:
    indent_num: int = docstring_util._get_indent_num_from_line(
        line='    any_value : int')
    assert indent_num == 1

    indent_num = docstring_util._get_indent_num_from_line(
        line='        any_value : int')
    assert indent_num == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_line_breaks_and_unnecessary_spaces() -> None:
    text: str = docstring_util._remove_line_breaks_and_unnecessary_spaces(
        text=(
            '    Lorem ipsum dolor sit amet, consectetur   '
            '\nadipiscing elit, sed do eiusmod  tempor incididunt '
            '\nut labore et dolore magna aliqua. '
        ))
    assert text == (
        'Lorem ipsum dolor sit amet, consectetur adipiscing '
        'elit, sed do eiusmod tempor incididunt ut labore et '
        'dolore magna aliqua.'
    )

_TEST_DOCSTRING: str = (
    '    """'
    '\n    Lorem ipsum dolor sit amet, consectetur '
    '\n    adipiscing elit, sed do eiusmod tempor incididunt '
    '\n    ut labore et dolore magna aliqua.'
    '\n'
    '\n    Parameters'
    '\n    ----------'
    '\n    test_param_1 : int'
    '\n        Ut enim ad minim veniam, quis nostrud exercitation'
    '\n        ullamco laboris nisi.'
    '\n    test_param_2 : str, optional'
    '\n        Ut aliquip ex ea commodo consequat.'
    '\n        Duis aute irure dolor in reprehenderit in'
    '\n        voluptate velit esse cillum dolore.'
    '\n'
    '\n        Omnis dolor repellendus. Temporibus autem quibusdam.'
    '\n'
    '\n    Returns'
    '\n    -------'
    '\n    test_return_val_1 : bool or int'
    '\n        Fugiat nulla pariatur. Excepteur sint occaecat '
    '\n        cupidatat non proident, sunt in culpa qui '
    '\n        officia deserunt mollit anim id est laborum.'
    '\n'
    '\n        Omnis dolor repellendus. Temporibus autem quibusdam.'
    '\n    test_return_val_2 : Sprite'
    '\n        Officiis debitis aut rerum necessitatibus saepe eveniet.'
    '\n'
    '\n    Notes'
    '\n    -----'
    '\n    At vero eos et accusamus et iusto odio dignissimos'
    '\n    ducimus, qui blanditiis praesentium voluptatum'
    '\n    deleniti atque corrupt.'
    '\n'
    '\n    Raises'
    '\n    ------'
    '\n    ValueError'
    '\n        Quos dolores et quas molestias excepturi sint,'
    '\n        obcaecati.'
    '\n    ImportError'
    '\n        Cupiditate non provident, similique sunt in culpa.'
    '\n'
    '\n    Examples'
    '\n    --------'
    '\n    >>> test_value_1: int = 10'
    '\n    >>> test_value_1'
    '\n    10'
    '\n'
    '\n    >>> test_value_2: int = test_function('
    '\n    ...    any_arg=10)'
    '\n    >>> test_value_2'
    '\n    30'
    '\n'
    '\n    References'
    '\n    ----------'
    '\n    - Test interface1 document'
    '\n        - https://en.wikipedia.org/test_page_1.html'
    '\n    - Test interface2 document'
    '\n        - https://en.wikipedia.org/test_page_2.html'
)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_param_or_rtn_values_from_docstring() -> None:
    param_or_rtn_values: List[_ParamOrRtnBase] = docstring_util.\
        _extract_param_or_rtn_values_from_docstring(
            target_type=_Parameter,
            docstring=_TEST_DOCSTRING)
    assert len(param_or_rtn_values) == 2
    for parameter_ in param_or_rtn_values:
        assert isinstance(parameter_, _Parameter)
    parameter: _Parameter = _Parameter(
        name='test_param_1',
        type_str='int',
        description=(
            'Ut enim ad minim veniam, quis nostrud exercitation '
            'ullamco laboris nisi.'
        ))
    assert param_or_rtn_values[0] == parameter
    parameter = _Parameter(
        name='test_param_2',
        type_str='str, optional',
        description=(
            'Ut aliquip ex ea commodo consequat. '
            'Duis aute irure dolor in reprehenderit in '
            'voluptate velit esse cillum dolore. '
            'Omnis dolor repellendus. Temporibus autem quibusdam.'
        ))
    assert param_or_rtn_values[1] == parameter

    param_or_rtn_values = docstring_util.\
        _extract_param_or_rtn_values_from_docstring(
            target_type=_Return,
            docstring=_TEST_DOCSTRING)
    assert len(param_or_rtn_values) == 2
    for return__ in param_or_rtn_values:
        assert isinstance(return__, _Return)
    return_: _Return = _Return(
        name='test_return_val_1',
        type_str='bool or int',
        description=(
            'Fugiat nulla pariatur. Excepteur sint occaecat '
            'cupidatat non proident, sunt in culpa qui '
            'officia deserunt mollit anim id est laborum. '
            'Omnis dolor repellendus. Temporibus autem quibusdam.'
        ))
    assert param_or_rtn_values[0] == return_
    return_ = _Return(
        name='test_return_val_2',
        type_str='Sprite',
        description=(
            'Officiis debitis aut rerum necessitatibus saepe eveniet.'
        ))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__make_description_from_lines_and_append_param_to_list() -> None:
    parameters: List[_ParamOrRtnBase] = []
    description_lines: List[str] = [
        '    At vero eos et accusamus et iusto odio dignissimos'
        '    ducimus, qui blanditiis praesentium voluptatum.'
    ]
    docstring_util._make_description_from_lines_and_append_param_to_list(
        target_type=_Parameter,
        param_or_rtn_values=parameters,
        value_name='test_value',
        value_type_str='int',
        description_lines=description_lines)
    parameter: _Parameter = _Parameter(
        name='test_value',
        type_str='int',
        description=(
            'At vero eos et accusamus et iusto odio dignissimos '
            'ducimus, qui blanditiis praesentium voluptatum.'
        ))
    assert parameters == [parameter]
    assert isinstance(parameters[0], _Parameter)
    assert description_lines == []


class Test_ParamOrRtnBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        param_or_rtn: _ParamOrRtnBase = _ParamOrRtnBase(
            name='test_value', type_str='int',
            description='Lorem ipsum dolor sit.')
        assert_attrs(
            expected_attrs={
                '_name': 'test_value',
                '_type_str': 'int',
                '_description': 'Lorem ipsum dolor sit.',
            },
            any_obj=param_or_rtn)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        param_or_rtn: _ParamOrRtnBase = _ParamOrRtnBase(
            name='test_value', type_str='int',
            description='Lorem ipsum dolor sit.')
        result: bool = param_or_rtn == 10
        assert not result

        other: _ParamOrRtnBase = _ParamOrRtnBase(
            name='test_value_2', type_str='int',
            description='Lorem ipsum dolor sit.')
        result = param_or_rtn == other
        assert not result

        other = _ParamOrRtnBase(
            name='test_value', type_str='str',
            description='Lorem ipsum dolor sit.')
        result = param_or_rtn == other
        assert not result

        other = _ParamOrRtnBase(
            name='test_value', type_str='int',
            description='Lorem ipsum dolor.')
        result = param_or_rtn == other
        assert not result

        other = _ParamOrRtnBase(
            name='test_value', type_str='int',
            description='Lorem ipsum dolor sit.')
        result = param_or_rtn == other
        assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_params_or_rtns_section_pattern_by_type() -> None:
    pattern: _ParamsOrRtnsSectionPattern = docstring_util.\
        _get_params_or_rtns_section_pattern_by_type(
            target_type=_Parameter)
    assert pattern == _ParamsOrRtnsSectionPattern.PARAMETERS

    pattern = docstring_util._get_params_or_rtns_section_pattern_by_type(
        target_type=_Return)
    assert pattern == _ParamsOrRtnsSectionPattern.RETURNS

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=docstring_util.
        _get_params_or_rtns_section_pattern_by_type,
        kwargs={'target_type': 10},
        match='Invalid type argument is provided: ',
    )
