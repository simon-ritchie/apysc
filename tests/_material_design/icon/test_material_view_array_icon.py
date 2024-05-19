from apysc._material_design.icon.material_view_array_icon import MaterialviewArrayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewArrayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewArrayIcon = MaterialviewArrayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
