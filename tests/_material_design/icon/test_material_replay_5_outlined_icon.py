from apysc._material_design.icon.material_replay_5_outlined_icon import (
    MaterialReplay5OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplay5OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplay5OutlinedIcon = MaterialReplay5OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
