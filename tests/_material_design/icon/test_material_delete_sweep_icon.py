from apysc._material_design.icon.material_delete_sweep_icon import MaterialdeleteSweepIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdeleteSweepIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdeleteSweepIcon = MaterialdeleteSweepIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
