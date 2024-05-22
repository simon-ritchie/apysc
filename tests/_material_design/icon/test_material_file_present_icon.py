from apysc._material_design.icon.material_file_present_icon import (
    MaterialFilePresentIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFilePresentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFilePresentIcon = MaterialFilePresentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
