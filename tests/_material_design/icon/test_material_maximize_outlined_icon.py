from apysc._material_design.icon.material_maximize_outlined_icon import MaterialmaximizeOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmaximizeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmaximizeOutlinedIcon = MaterialmaximizeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
