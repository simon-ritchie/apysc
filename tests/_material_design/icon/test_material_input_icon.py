from apysc._material_design.icon.material_input_icon import MaterialInputIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInputIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInputIcon = MaterialInputIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
