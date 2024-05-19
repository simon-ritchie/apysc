from apysc._material_design.icon.material_alternate_email_icon import MaterialalternateEmailIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialalternateEmailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialalternateEmailIcon = MaterialalternateEmailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
