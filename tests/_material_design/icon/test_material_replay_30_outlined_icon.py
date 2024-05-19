from apysc._material_design.icon.material_replay_30_outlined_icon import Materialreplay30OutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplay30OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialreplay30OutlinedIcon = Materialreplay30OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
