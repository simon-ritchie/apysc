from apysc._material_design.icon.material_build_icon import MaterialBuildIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBuildIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBuildIcon = MaterialBuildIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
