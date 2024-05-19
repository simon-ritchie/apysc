from apysc._material_design.icon.material_play_for_work_icon import MaterialplayForWorkIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplayForWorkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplayForWorkIcon = MaterialplayForWorkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
