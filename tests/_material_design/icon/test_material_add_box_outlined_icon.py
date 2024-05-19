from apysc._material_design.icon.material_add_box_outlined_icon import MaterialaddBoxOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddBoxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddBoxOutlinedIcon = MaterialaddBoxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
