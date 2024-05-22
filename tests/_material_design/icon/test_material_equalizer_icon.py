from apysc._material_design.icon.material_equalizer_icon import MaterialEqualizerIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEqualizerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEqualizerIcon = MaterialEqualizerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
