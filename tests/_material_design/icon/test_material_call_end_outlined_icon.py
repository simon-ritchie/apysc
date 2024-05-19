from apysc._material_design.icon.material_call_end_outlined_icon import MaterialcallEndOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallEndOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallEndOutlinedIcon = MaterialcallEndOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
