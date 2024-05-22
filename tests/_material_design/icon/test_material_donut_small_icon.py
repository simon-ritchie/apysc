from apysc._material_design.icon.material_donut_small_icon import MaterialDonutSmallIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDonutSmallIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDonutSmallIcon = MaterialDonutSmallIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
