from apysc._material_design.icon.material_find_replace_outlined_icon import (
    MaterialFindReplaceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFindReplaceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFindReplaceOutlinedIcon = MaterialFindReplaceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
