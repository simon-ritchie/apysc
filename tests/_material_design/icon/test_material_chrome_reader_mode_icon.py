from apysc._material_design.icon.material_chrome_reader_mode_icon import MaterialchromeReaderModeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialchromeReaderModeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialchromeReaderModeIcon = MaterialchromeReaderModeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
