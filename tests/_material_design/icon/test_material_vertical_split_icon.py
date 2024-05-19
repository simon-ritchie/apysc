from apysc._material_design.icon.material_vertical_split_icon import MaterialverticalSplitIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialverticalSplitIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialverticalSplitIcon = MaterialverticalSplitIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
