from apysc._material_design.icon.material_horizontal_split_outlined_icon import (
    MaterialHorizontalSplitOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHorizontalSplitOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHorizontalSplitOutlinedIcon = (
            MaterialHorizontalSplitOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
