from apysc._material_design.icon.material_view_list_icon import MaterialviewListIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewListIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewListIcon = MaterialviewListIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
