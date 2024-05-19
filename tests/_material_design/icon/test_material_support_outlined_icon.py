from apysc._material_design.icon.material_support_outlined_icon import MaterialsupportOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsupportOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsupportOutlinedIcon = MaterialsupportOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
