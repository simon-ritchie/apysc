from apysc._material_design.icon.material_replay_5_icon import MaterialReplay5Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplay5Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplay5Icon = MaterialReplay5Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
