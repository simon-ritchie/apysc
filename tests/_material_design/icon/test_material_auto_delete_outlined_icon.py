from apysc._material_design.icon.material_auto_delete_outlined_icon import (
    MaterialautoDeleteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialautoDeleteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialautoDeleteOutlinedIcon = MaterialautoDeleteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
