from apysc._material_design.icon.material_exit_to_app_icon import MaterialExitToAppIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExitToAppIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExitToAppIcon = MaterialExitToAppIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
