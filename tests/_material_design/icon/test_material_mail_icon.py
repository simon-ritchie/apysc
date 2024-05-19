from apysc._material_design.icon.material_mail_icon import MaterialmailIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmailIcon = MaterialmailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
