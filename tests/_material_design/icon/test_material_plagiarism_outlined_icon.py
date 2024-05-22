from apysc._material_design.icon.material_plagiarism_outlined_icon import (
    MaterialPlagiarismOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlagiarismOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlagiarismOutlinedIcon = MaterialPlagiarismOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
