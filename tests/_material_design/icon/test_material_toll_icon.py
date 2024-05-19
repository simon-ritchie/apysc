from apysc._material_design.icon.material_toll_icon import MaterialtollIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtollIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtollIcon = MaterialtollIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
