from apysc._material_design.icon.material_assessment_icon import MaterialAssessmentIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssessmentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssessmentIcon = MaterialAssessmentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
