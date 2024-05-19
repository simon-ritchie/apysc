from apysc._material_design.icon.material_shuffle_icon import MaterialshuffleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshuffleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshuffleIcon = MaterialshuffleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
