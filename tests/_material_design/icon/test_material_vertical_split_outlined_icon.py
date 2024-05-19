from apysc._material_design.icon.material_vertical_split_outlined_icon import MaterialverticalSplitOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialverticalSplitOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialverticalSplitOutlinedIcon = MaterialverticalSplitOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
