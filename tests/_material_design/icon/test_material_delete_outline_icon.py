from apysc._material_design.icon.material_delete_outline_icon import (
    MaterialdeleteOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdeleteOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdeleteOutlineIcon = MaterialdeleteOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
