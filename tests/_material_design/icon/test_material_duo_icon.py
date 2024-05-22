from apysc._material_design.icon.material_duo_icon import MaterialDuoIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDuoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDuoIcon = MaterialDuoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
