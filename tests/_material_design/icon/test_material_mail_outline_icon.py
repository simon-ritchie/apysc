from apysc._material_design.icon.material_mail_outline_icon import MaterialmailOutlineIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmailOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmailOutlineIcon = MaterialmailOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
