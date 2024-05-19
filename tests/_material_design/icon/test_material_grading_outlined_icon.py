from apysc._material_design.icon.material_grading_outlined_icon import MaterialgradingOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgradingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgradingOutlinedIcon = MaterialgradingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
