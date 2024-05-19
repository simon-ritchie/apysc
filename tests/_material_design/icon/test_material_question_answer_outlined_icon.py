from apysc._material_design.icon.material_question_answer_outlined_icon import (
    MaterialquestionAnswerOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialquestionAnswerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialquestionAnswerOutlinedIcon = MaterialquestionAnswerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
