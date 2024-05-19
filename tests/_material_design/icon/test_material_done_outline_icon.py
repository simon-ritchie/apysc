from apysc._material_design.icon.material_done_outline_icon import MaterialdoneOutlineIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdoneOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdoneOutlineIcon = MaterialdoneOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
