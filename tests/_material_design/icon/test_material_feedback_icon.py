from apysc._material_design.icon.material_feedback_icon import MaterialfeedbackIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfeedbackIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfeedbackIcon = MaterialfeedbackIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
