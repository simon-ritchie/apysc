from apysc._material_design.icon.material_add_icon import MaterialAddIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddIcon = MaterialAddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
