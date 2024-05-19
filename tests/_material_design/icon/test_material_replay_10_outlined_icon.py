from apysc._material_design.icon.material_replay_10_outlined_icon import Materialreplay10OutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplay10OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialreplay10OutlinedIcon = Materialreplay10OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
