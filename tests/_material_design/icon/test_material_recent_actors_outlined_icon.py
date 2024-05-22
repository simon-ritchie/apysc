from apysc._material_design.icon.material_recent_actors_outlined_icon import (
    MaterialRecentActorsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRecentActorsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRecentActorsOutlinedIcon = MaterialRecentActorsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
