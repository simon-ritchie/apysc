from random import randint

from retrying import retry

from apysc._lint_and_doc import document_text_split_util
from apysc._lint_and_doc.document_text_split_util import Heading, BodyText
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
