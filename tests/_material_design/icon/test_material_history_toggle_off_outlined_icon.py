from apysc._material_design.icon.material_history_toggle_off_outlined_icon import MaterialhistoryToggleOffOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhistoryToggleOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhistoryToggleOffOutlinedIcon = MaterialhistoryToggleOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
