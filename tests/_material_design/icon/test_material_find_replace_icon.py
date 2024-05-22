from apysc._material_design.icon.material_find_replace_icon import (
    MaterialFindReplaceIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFindReplaceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFindReplaceIcon = MaterialFindReplaceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
