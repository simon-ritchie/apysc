from apysc._material_design.icon.material_closed_caption_disabled_outlined_icon import MaterialclosedCaptionDisabledOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclosedCaptionDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclosedCaptionDisabledOutlinedIcon = MaterialclosedCaptionDisabledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
