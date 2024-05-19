from apysc._material_design.icon.material_insights_outlined_icon import MaterialinsightsOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinsightsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinsightsOutlinedIcon = MaterialinsightsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
