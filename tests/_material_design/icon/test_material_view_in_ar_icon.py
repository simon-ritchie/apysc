from apysc._material_design.icon.material_view_in_ar_icon import MaterialviewInArIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewInArIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewInArIcon = MaterialviewInArIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
