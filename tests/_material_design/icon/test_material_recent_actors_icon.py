from apysc._material_design.icon.material_recent_actors_icon import (
    MaterialRecentActorsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRecentActorsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRecentActorsIcon = MaterialRecentActorsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
