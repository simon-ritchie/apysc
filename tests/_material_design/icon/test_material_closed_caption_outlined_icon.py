from apysc._material_design.icon.material_closed_caption_outlined_icon import (
    MaterialClosedCaptionOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialClosedCaptionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialClosedCaptionOutlinedIcon = MaterialClosedCaptionOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
