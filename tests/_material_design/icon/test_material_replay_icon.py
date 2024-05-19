from apysc._material_design.icon.material_replay_icon import MaterialreplayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreplayIcon = MaterialreplayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
