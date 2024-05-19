from apysc._material_design.icon.material_theaters_icon import MaterialtheatersIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtheatersIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtheatersIcon = MaterialtheatersIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
