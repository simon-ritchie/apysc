from apysc._material_design.icon.material_done_icon import MaterialDoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDoneIcon = MaterialDoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
