from apysc._material_design.icon.material_table_view_outlined_icon import (
    MaterialTableViewOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTableViewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTableViewOutlinedIcon = MaterialTableViewOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
