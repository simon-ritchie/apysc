from apysc._material_design.icon.material_theaters_icon import MaterialTheatersIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTheatersIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTheatersIcon = MaterialTheatersIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
