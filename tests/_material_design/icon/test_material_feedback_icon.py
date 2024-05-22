from apysc._material_design.icon.material_feedback_icon import MaterialFeedbackIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFeedbackIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFeedbackIcon = MaterialFeedbackIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
