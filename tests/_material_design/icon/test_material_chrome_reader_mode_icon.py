from apysc._material_design.icon.material_chrome_reader_mode_icon import (
    MaterialChromeReaderModeIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChromeReaderModeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChromeReaderModeIcon = MaterialChromeReaderModeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
