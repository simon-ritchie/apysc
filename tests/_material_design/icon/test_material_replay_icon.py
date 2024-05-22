from apysc._material_design.icon.material_replay_icon import MaterialReplayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplayIcon = MaterialReplayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
