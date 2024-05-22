from apysc._material_design.icon.material_grade_outlined_icon import (
    MaterialGradeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGradeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGradeOutlinedIcon = MaterialGradeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
