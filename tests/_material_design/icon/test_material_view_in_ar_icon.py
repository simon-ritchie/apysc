from apysc._material_design.icon.material_view_in_ar_icon import MaterialViewInArIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewInArIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewInArIcon = MaterialViewInArIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
