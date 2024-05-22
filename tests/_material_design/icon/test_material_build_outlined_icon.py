from apysc._material_design.icon.material_build_outlined_icon import (
    MaterialBuildOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBuildOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBuildOutlinedIcon = MaterialBuildOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
