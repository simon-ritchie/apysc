from apysc._material_design.icon.material_phonelink_erase_icon import MaterialphonelinkEraseIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphonelinkEraseIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphonelinkEraseIcon = MaterialphonelinkEraseIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
