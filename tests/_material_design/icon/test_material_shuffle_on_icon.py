from apysc._material_design.icon.material_shuffle_on_icon import MaterialshuffleOnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshuffleOnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshuffleOnIcon = MaterialshuffleOnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
