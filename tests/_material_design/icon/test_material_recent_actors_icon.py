from apysc._material_design.icon.material_recent_actors_icon import MaterialrecentActorsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrecentActorsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrecentActorsIcon = MaterialrecentActorsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
