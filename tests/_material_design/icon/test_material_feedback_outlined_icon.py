from apysc._material_design.icon.material_feedback_outlined_icon import (
    MaterialfeedbackOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfeedbackOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfeedbackOutlinedIcon = MaterialfeedbackOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
