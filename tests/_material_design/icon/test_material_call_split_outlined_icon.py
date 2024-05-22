from apysc._material_design.icon.material_call_split_outlined_icon import (
    MaterialCallSplitOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallSplitOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallSplitOutlinedIcon = MaterialCallSplitOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
