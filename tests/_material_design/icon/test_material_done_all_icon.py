from apysc._material_design.icon.material_done_all_icon import MaterialDoneAllIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDoneAllIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDoneAllIcon = MaterialDoneAllIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
