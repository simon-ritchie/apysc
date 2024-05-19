from apysc._material_design.icon.material_phonelink_setup_icon import MaterialphonelinkSetupIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphonelinkSetupIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphonelinkSetupIcon = MaterialphonelinkSetupIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
