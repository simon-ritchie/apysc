from apysc._material_design.icon.material_grading_icon import MaterialGradingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGradingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGradingIcon = MaterialGradingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
