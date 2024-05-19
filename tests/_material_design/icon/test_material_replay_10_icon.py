from apysc._material_design.icon.material_replay_10_icon import Materialreplay10Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplay10Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialreplay10Icon = Materialreplay10Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
