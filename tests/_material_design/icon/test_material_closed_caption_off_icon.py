from apysc._material_design.icon.material_closed_caption_off_icon import MaterialclosedCaptionOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclosedCaptionOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclosedCaptionOffIcon = MaterialclosedCaptionOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
