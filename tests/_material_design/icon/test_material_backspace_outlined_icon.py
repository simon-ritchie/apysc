from apysc._material_design.icon.material_backspace_outlined_icon import (
    MaterialbackspaceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbackspaceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbackspaceOutlinedIcon = MaterialbackspaceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
