from apysc._material_design.icon.material_mark_email_read_outlined_icon import (
    MaterialMarkEmailReadOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkEmailReadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkEmailReadOutlinedIcon = MaterialMarkEmailReadOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
