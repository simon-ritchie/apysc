from apysc._material_design.icon.material_notification_important_icon import MaterialnotificationImportantIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnotificationImportantIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnotificationImportantIcon = MaterialnotificationImportantIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
