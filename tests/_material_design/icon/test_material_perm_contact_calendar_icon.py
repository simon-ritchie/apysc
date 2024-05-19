from apysc._material_design.icon.material_perm_contact_calendar_icon import MaterialpermContactCalendarIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermContactCalendarIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermContactCalendarIcon = MaterialpermContactCalendarIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
