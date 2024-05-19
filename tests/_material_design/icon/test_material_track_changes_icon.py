from apysc._material_design.icon.material_track_changes_icon import MaterialtrackChangesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtrackChangesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtrackChangesIcon = MaterialtrackChangesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
