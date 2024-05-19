from apysc._material_design.icon.material_grading_icon import MaterialgradingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgradingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgradingIcon = MaterialgradingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
