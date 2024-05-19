from apysc._material_design.icon.material_anchor_outlined_icon import MaterialanchorOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialanchorOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialanchorOutlinedIcon = MaterialanchorOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
