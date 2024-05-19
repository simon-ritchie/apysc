from apysc._material_design.icon.material_insights_icon import MaterialinsightsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinsightsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinsightsIcon = MaterialinsightsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
