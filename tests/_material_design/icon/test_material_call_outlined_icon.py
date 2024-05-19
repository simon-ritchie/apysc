from apysc._material_design.icon.material_call_outlined_icon import MaterialcallOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallOutlinedIcon = MaterialcallOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
