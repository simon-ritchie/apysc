from apysc._material_design.icon.material_check_circle_icon import MaterialcheckCircleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcheckCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcheckCircleIcon = MaterialcheckCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
