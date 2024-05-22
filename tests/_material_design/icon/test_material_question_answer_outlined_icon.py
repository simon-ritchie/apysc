from apysc._material_design.icon.material_question_answer_outlined_icon import (
    MaterialQuestionAnswerOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQuestionAnswerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQuestionAnswerOutlinedIcon = MaterialQuestionAnswerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
