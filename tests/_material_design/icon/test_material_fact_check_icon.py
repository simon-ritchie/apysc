from apysc._material_design.icon.material_fact_check_icon import MaterialfactCheckIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfactCheckIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfactCheckIcon = MaterialfactCheckIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
