from apysc._material_design.icon.material_equalizer_icon import MaterialequalizerIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialequalizerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialequalizerIcon = MaterialequalizerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
