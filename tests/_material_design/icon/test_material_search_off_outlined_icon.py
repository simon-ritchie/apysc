from apysc._material_design.icon.material_search_off_outlined_icon import (
    MaterialSearchOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSearchOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSearchOffOutlinedIcon = MaterialSearchOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
