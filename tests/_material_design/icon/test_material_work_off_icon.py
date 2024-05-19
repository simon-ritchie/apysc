from apysc._material_design.icon.material_work_off_icon import MaterialworkOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialworkOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialworkOffIcon = MaterialworkOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
