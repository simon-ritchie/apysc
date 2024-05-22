from apysc._material_design.icon.material_fiber_new_icon import MaterialFiberNewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFiberNewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFiberNewIcon = MaterialFiberNewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
