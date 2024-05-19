from apysc._material_design.icon.material_turned_in_icon import MaterialturnedInIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialturnedInIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialturnedInIcon = MaterialturnedInIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
