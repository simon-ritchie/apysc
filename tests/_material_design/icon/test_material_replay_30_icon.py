from apysc._material_design.icon.material_replay_30_icon import MaterialReplay30Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplay30Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplay30Icon = MaterialReplay30Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
