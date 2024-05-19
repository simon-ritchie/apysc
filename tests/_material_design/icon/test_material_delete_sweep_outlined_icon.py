from apysc._material_design.icon.material_delete_sweep_outlined_icon import MaterialdeleteSweepOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdeleteSweepOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdeleteSweepOutlinedIcon = MaterialdeleteSweepOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
