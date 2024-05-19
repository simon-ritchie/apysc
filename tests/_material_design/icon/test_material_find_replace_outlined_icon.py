from apysc._material_design.icon.material_find_replace_outlined_icon import (
    MaterialfindReplaceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfindReplaceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfindReplaceOutlinedIcon = MaterialfindReplaceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
