from apysc._material_design.icon.material_closed_caption_disabled_icon import (
    MaterialClosedCaptionDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialClosedCaptionDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialClosedCaptionDisabledIcon = MaterialClosedCaptionDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
