from apysc._material_design.icon.material_replay_10_icon import MaterialReplay10Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplay10Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplay10Icon = MaterialReplay10Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
