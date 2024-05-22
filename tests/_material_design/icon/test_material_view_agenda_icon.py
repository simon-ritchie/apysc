from apysc._material_design.icon.material_view_agenda_icon import MaterialViewAgendaIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewAgendaIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewAgendaIcon = MaterialViewAgendaIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
