from apysc._material_design.icon.material_closed_caption_disabled_icon import (
    MaterialclosedCaptionDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclosedCaptionDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclosedCaptionDisabledIcon = MaterialclosedCaptionDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
