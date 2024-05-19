from apysc._material_design.icon.material_low_priority_icon import MateriallowPriorityIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallowPriorityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallowPriorityIcon = MateriallowPriorityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
