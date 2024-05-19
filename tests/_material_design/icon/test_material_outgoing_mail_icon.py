from apysc._material_design.icon.material_outgoing_mail_icon import MaterialoutgoingMailIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialoutgoingMailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialoutgoingMailIcon = MaterialoutgoingMailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
