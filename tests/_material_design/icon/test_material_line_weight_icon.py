from apysc._material_design.icon.material_line_weight_icon import MaterialLineWeightIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLineWeightIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLineWeightIcon = MaterialLineWeightIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
