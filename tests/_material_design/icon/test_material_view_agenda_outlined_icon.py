from apysc._material_design.icon.material_view_agenda_outlined_icon import (
    MaterialViewAgendaOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewAgendaOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewAgendaOutlinedIcon = MaterialViewAgendaOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
