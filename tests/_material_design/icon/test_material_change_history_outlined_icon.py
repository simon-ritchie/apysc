from apysc._material_design.icon.material_change_history_outlined_icon import MaterialchangeHistoryOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialchangeHistoryOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialchangeHistoryOutlinedIcon = MaterialchangeHistoryOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
