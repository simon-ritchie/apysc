from apysc._material_design.icon.material_font_download_outlined_icon import MaterialfontDownloadOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfontDownloadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfontDownloadOutlinedIcon = MaterialfontDownloadOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
