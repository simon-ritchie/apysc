from apysc._material_design.icon.material_history_outlined_icon import MaterialhistoryOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhistoryOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhistoryOutlinedIcon = MaterialhistoryOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
