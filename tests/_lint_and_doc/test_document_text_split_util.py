from random import randint
from typing import List, Union

from retrying import retry

from apysc._lint_and_doc import document_text_split_util
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText, CodeBlock
from tests.testing_helper import assert_attrs


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
    splitted: List[Union[Heading, BodyText, CodeBlock]] = []
    document_text_split_util.\
        _create_body_text_and_append_to_list_if_values_exist(
            splitted=splitted, body_text_lines=[])
    assert splitted == []

    body_text_lines: List[str] = [
        '',
        'Lorem ipsum dolor sit amet.',
        'consectetur adipiscing.',
        '',
    ]
    document_text_split_util.\
        _create_body_text_and_append_to_list_if_values_exist(
            splitted=splitted, body_text_lines=body_text_lines)
    assert len(splitted) == 1
    body_text = splitted[0]
    if not isinstance(body_text, BodyText):
        raise AssertionError(
            f'Returned value\'s type is invalid: {type(body_text)}')
    assert body_text.text == (
        'Lorem ipsum dolor sit amet.\nconsectetur adipiscing.'
    )
