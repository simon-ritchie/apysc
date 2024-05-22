from apysc._material_design.icon.material_assessment_outlined_icon import (
    MaterialAssessmentOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssessmentOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssessmentOutlinedIcon = MaterialAssessmentOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
