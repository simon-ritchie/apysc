from apysc._material_design.icon.material_view_list_icon import MaterialViewListIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewListIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewListIcon = MaterialViewListIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
