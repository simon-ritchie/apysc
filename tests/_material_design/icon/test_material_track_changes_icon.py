from apysc._material_design.icon.material_track_changes_icon import (
    MaterialTrackChangesIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTrackChangesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTrackChangesIcon = MaterialTrackChangesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
