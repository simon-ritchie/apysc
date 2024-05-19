from apysc._material_design.icon.material_attribution_outlined_icon import MaterialattributionOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialattributionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialattributionOutlinedIcon = MaterialattributionOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
