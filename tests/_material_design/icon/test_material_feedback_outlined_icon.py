from apysc._material_design.icon.material_feedback_outlined_icon import (
    MaterialFeedbackOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFeedbackOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFeedbackOutlinedIcon = MaterialFeedbackOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
