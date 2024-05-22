from apysc._material_design.icon.material_horizontal_split_icon import (
    MaterialHorizontalSplitIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHorizontalSplitIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHorizontalSplitIcon = MaterialHorizontalSplitIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
