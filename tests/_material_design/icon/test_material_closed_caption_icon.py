from apysc._material_design.icon.material_closed_caption_icon import (
    MaterialclosedCaptionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclosedCaptionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclosedCaptionIcon = MaterialclosedCaptionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
