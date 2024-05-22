from apysc._material_design.icon.material_dangerous_icon import MaterialDangerousIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDangerousIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDangerousIcon = MaterialDangerousIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
