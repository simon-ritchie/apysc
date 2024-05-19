from apysc._material_design.icon.material_chrome_reader_mode_outlined_icon import (
    MaterialchromeReaderModeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialchromeReaderModeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialchromeReaderModeOutlinedIcon = (
            MaterialchromeReaderModeOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
