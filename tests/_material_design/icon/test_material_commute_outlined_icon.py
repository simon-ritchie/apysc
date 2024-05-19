from apysc._material_design.icon.material_commute_outlined_icon import MaterialcommuteOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcommuteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcommuteOutlinedIcon = MaterialcommuteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
