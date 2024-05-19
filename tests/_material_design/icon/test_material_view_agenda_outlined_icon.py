from apysc._material_design.icon.material_view_agenda_outlined_icon import MaterialviewAgendaOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewAgendaOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewAgendaOutlinedIcon = MaterialviewAgendaOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
