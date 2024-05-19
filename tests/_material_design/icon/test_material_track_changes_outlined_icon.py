from apysc._material_design.icon.material_track_changes_outlined_icon import (
    MaterialtrackChangesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtrackChangesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtrackChangesOutlinedIcon = MaterialtrackChangesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
