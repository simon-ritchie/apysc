from apysc._material_design.icon.material_question_answer_icon import (
    MaterialQuestionAnswerIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQuestionAnswerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQuestionAnswerIcon = MaterialQuestionAnswerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
