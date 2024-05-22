from apysc._material_design.icon.material_content_paste_outlined_icon import (
    MaterialContentPasteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContentPasteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContentPasteOutlinedIcon = MaterialContentPasteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
