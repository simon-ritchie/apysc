from apysc._material_design.icon.material_build_outlined_icon import MaterialbuildOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbuildOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbuildOutlinedIcon = MaterialbuildOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
