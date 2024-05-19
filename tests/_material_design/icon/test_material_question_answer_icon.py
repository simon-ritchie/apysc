from apysc._material_design.icon.material_question_answer_icon import (
    MaterialquestionAnswerIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialquestionAnswerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialquestionAnswerIcon = MaterialquestionAnswerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
