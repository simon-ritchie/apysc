from random import randint
from typing import List
from typing import Union

from retrying import retry

from apysc._lint_and_doc import document_text_split_util
from apysc._lint_and_doc.document_text_split_util import BodyText
from apysc._lint_and_doc.document_text_split_util import CodeBlock
from apysc._lint_and_doc.document_text_split_util import Heading
from apysc._testing.testing_helper import assert_attrs


class TestHeading:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        heading: Heading = Heading(
            heading_text='## What is the Sprite?')
        assert_attrs(
            expected_attrs={
                '_text': 'What is the Sprite?',
                '_overall_text': '## What is the Sprite?',
                '_sharp_num': 2,
            },
            any_obj=heading)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_text(self) -> None:
        heading: Heading = Heading(
            heading_text='## What is the Sprite?')
        assert heading.text == 'What is the Sprite?'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_overall_text(self) -> None:
        heading: Heading = Heading(
            heading_text='## What is the Sprite?')
        assert heading.overall_text == '## What is the Sprite?'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_sharp_num(self) -> None:
        heading: Heading = Heading(
            heading_text='## What is the Sprite?')
        assert heading.sharp_num == 2


class TestBodyText:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        body_text: BodyText = BodyText(
            text='\n\nLorem ipsum dolor sit amet.\n\n')
        assert_attrs(
            expected_attrs={
                '_text': 'Lorem ipsum dolor sit amet.'
            },
            any_obj=body_text)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_text(self) -> None:
        body_text: BodyText = BodyText(
            text='\n\nLorem ipsum dolor sit amet.\n\n')
        assert body_text.text == 'Lorem ipsum dolor sit amet.'


_TEST_CODE_BLOCK_1: str = '''
```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='sprite_graphics_attribute/')
```
'''

_TEST_CODE_BLOCK_2: str = '''import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='sprite_graphics_attribute/')'''

_TEST_MARKDOWN_TEXT: str = (
    '# Sprite'
    '\n\nThis page explains the `Sprite` class.'
    '\n\n## What is the Sprite?'
    '\n\nThe `Sprite` class is the container of each '
    '`DisplayObject` instance. It also has the '
    '`Graphics` class interfaces and can draw each '
    'vector graphic.'
    '\n\n## graphics attribute interfaces'
    '\n\nThe `Sprite` instance has the `graphics` attribute, '
    'and you can draw each vector graphic with it.'
    '\n\n```py'
    '\n# runnable'
    '\nimport apysc as ap'
    '\nap.Stage()'
    '\n```'
    '\n\n<iframe src="static/sprite_graphics_attribute/index.html" '
    'width="150" height="150"></iframe>'
)


class TestCodeBlock:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        code_block: CodeBlock = CodeBlock(
            code_block=_TEST_CODE_BLOCK_1)
        assert_attrs(
            expected_attrs={
                '_code_block': _TEST_CODE_BLOCK_2,
                '_overall_code_block': _TEST_CODE_BLOCK_1.strip(),
                '_code_type': 'py',
            },
            any_obj=code_block)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_code_block(self) -> None:
        code_block: CodeBlock = CodeBlock(
            code_block=_TEST_CODE_BLOCK_1)
        assert code_block.code_block == _TEST_CODE_BLOCK_2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_overall_code_block(self) -> None:
        code_block: CodeBlock = CodeBlock(
            code_block=_TEST_CODE_BLOCK_1)
        assert code_block.overall_code_block == _TEST_CODE_BLOCK_1.strip()

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_code_type(self) -> None:
        code_block: CodeBlock = CodeBlock(
            code_block=_TEST_CODE_BLOCK_1)
        assert code_block.code_type == 'py'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_code_block_from_list() -> None:
    code_block_lines: List[str] = [
        '```py',
        'import apysc as ap',
        "ap.trace('Hello!')",
        '```',
    ]
    code_block: CodeBlock = document_text_split_util.\
        _create_code_block_from_list(
            code_block_lines=code_block_lines)
    assert code_block_lines == []
    assert code_block.code_block == (
        'import apysc as ap'
        "\nap.trace('Hello!')"
    )
    assert code_block.code_type == 'py'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_body_text_and_append_to_list_if_values_exist() -> None:
    splitted_values: List[Union[Heading, BodyText, CodeBlock]] = []
    document_text_split_util.\
        _create_body_text_and_append_to_list_if_values_exist(
            splitted_values=splitted_values, body_text_lines=[])
    assert splitted_values == []

    body_text_lines: List[str] = [
        '',
        'Lorem ipsum dolor sit amet.',
        'consectetur adipiscing.',
        '',
    ]
    document_text_split_util.\
        _create_body_text_and_append_to_list_if_values_exist(
            splitted_values=splitted_values, body_text_lines=body_text_lines)
    assert len(splitted_values) == 1
    body_text = splitted_values[0]
    if not isinstance(body_text, BodyText):
        raise AssertionError(
            f'Returned value\'s type is invalid: {type(body_text)}')
    assert body_text.text == (
        'Lorem ipsum dolor sit amet.\nconsectetur adipiscing.'
    )
    assert body_text_lines == []


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_split_markdown_document() -> None:
    splitted: List[Union[Heading, BodyText, CodeBlock]] = \
        document_text_split_util.split_markdown_document(
            markdown_txt=_TEST_MARKDOWN_TEXT)
    assert len(splitted) == 8

    heading_1 = splitted[0]
    if not isinstance(heading_1, Heading):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(heading_1)}')
    assert heading_1.text == 'Sprite'

    body_text_1 = splitted[1]
    if not isinstance(body_text_1, BodyText):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(body_text_1)}')
    assert body_text_1.text == 'This page explains the `Sprite` class.'

    heading_2 = splitted[2]
    if not isinstance(heading_2, Heading):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(heading_2)}')
    assert heading_2.text == 'What is the Sprite?'

    body_text_2 = splitted[3]
    if not isinstance(body_text_2, BodyText):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(body_text_2)}')
    assert body_text_2.text == (
        'The `Sprite` class is the container of each '
        '`DisplayObject` instance. It also has the '
        '`Graphics` class interfaces and can draw each '
        'vector graphic.'
    )

    heading_3 = splitted[4]
    if not isinstance(heading_3, Heading):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(heading_3)}')
    assert heading_3.text == 'graphics attribute interfaces'

    body_text_3 = splitted[5]
    if not isinstance(body_text_3, BodyText):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(body_text_3)}')
    assert body_text_3.text == (
        'The `Sprite` instance has the `graphics` attribute, '
        'and you can draw each vector graphic with it.'
    )

    code_block_1 = splitted[6]
    if not isinstance(code_block_1, CodeBlock):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(code_block_1)}')
    assert code_block_1.code_block == (
        'import apysc as ap'
        '\nap.Stage()'
    )

    body_text_4 = splitted[7]
    if not isinstance(body_text_4, BodyText):
        raise AssertionError(
            f'A returned value\'s type is invalid: {type(body_text_4)}')
    assert body_text_4.text == (
        '<iframe src="static/sprite_graphics_attribute/index.html" '
        'width="150" height="150"></iframe>'
    )
