from apysc._material_design.icon.material_email_icon import MaterialEmailIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEmailIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEmailIcon = MaterialEmailIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
