from apysc._material_design.icon.material_important_devices_outlined_icon import MaterialimportantDevicesOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialimportantDevicesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialimportantDevicesOutlinedIcon = MaterialimportantDevicesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
