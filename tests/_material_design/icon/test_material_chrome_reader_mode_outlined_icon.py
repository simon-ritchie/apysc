from apysc._material_design.icon.material_chrome_reader_mode_outlined_icon import (
    MaterialChromeReaderModeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChromeReaderModeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChromeReaderModeOutlinedIcon = (
            MaterialChromeReaderModeOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
