from apysc._material_design.icon.material_view_list_outlined_icon import (
    MaterialviewListOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewListOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewListOutlinedIcon = MaterialviewListOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
