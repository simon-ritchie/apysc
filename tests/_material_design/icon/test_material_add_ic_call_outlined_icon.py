from apysc._material_design.icon.material_add_ic_call_outlined_icon import MaterialaddIcCallOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddIcCallOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddIcCallOutlinedIcon = MaterialaddIcCallOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
