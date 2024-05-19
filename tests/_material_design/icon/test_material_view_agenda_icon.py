from apysc._material_design.icon.material_view_agenda_icon import MaterialviewAgendaIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewAgendaIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewAgendaIcon = MaterialviewAgendaIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
