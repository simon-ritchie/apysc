from apysc._material_design.icon.material_shuffle_on_icon import MaterialShuffleOnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialShuffleOnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialShuffleOnIcon = MaterialShuffleOnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
