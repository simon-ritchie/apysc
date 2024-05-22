from apysc._material_design.icon.material_not_accessible_outlined_icon import (
    MaterialNotAccessibleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNotAccessibleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNotAccessibleOutlinedIcon = MaterialNotAccessibleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
