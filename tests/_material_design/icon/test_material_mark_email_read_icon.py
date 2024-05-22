from apysc._material_design.icon.material_mark_email_read_icon import (
    MaterialMarkEmailReadIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkEmailReadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkEmailReadIcon = MaterialMarkEmailReadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
