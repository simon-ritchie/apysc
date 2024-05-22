from apysc._material_design.icon.material_reorder_icon import MaterialReorderIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReorderIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReorderIcon = MaterialReorderIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
