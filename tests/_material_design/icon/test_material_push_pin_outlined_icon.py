from apysc._material_design.icon.material_push_pin_outlined_icon import MaterialpushPinOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpushPinOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpushPinOutlinedIcon = MaterialpushPinOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
