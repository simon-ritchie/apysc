from apysc._material_design.icon.material_flaky_icon import MaterialFlakyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFlakyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFlakyIcon = MaterialFlakyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
