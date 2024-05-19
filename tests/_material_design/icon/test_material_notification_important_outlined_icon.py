from apysc._material_design.icon.material_notification_important_outlined_icon import MaterialnotificationImportantOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnotificationImportantOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnotificationImportantOutlinedIcon = MaterialnotificationImportantOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
