from apysc._material_design.icon.material_dialpad_icon import MaterialDialpadIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDialpadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDialpadIcon = MaterialDialpadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
