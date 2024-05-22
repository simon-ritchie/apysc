from apysc._material_design.icon.material_important_devices_outlined_icon import (
    MaterialImportantDevicesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialImportantDevicesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialImportantDevicesOutlinedIcon = (
            MaterialImportantDevicesOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
