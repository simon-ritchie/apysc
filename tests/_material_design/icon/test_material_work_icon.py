from apysc._material_design.icon.material_work_icon import MaterialWorkIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWorkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWorkIcon = MaterialWorkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
