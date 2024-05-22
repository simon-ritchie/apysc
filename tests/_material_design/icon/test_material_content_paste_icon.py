from apysc._material_design.icon.material_content_paste_icon import (
    MaterialContentPasteIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContentPasteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContentPasteIcon = MaterialContentPasteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
