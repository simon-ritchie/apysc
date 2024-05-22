from apysc._material_design.icon.material_work_off_icon import MaterialWorkOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWorkOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWorkOffIcon = MaterialWorkOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
