from apysc._material_design.icon.material_outgoing_mail_icon import (
    MaterialOutgoingMailIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOutgoingMailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOutgoingMailIcon = MaterialOutgoingMailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
