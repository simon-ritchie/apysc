from apysc._material_design.icon.material_file_copy_outlined_icon import (
    MaterialFileCopyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFileCopyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFileCopyOutlinedIcon = MaterialFileCopyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
