from apysc._material_design.icon.material_equalizer_outlined_icon import MaterialequalizerOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialequalizerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialequalizerOutlinedIcon = MaterialequalizerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
