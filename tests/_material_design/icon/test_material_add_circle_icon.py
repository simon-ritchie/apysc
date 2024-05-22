from apysc._material_design.icon.material_add_circle_icon import MaterialAddCircleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddCircleIcon = MaterialAddCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
