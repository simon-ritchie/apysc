from apysc._material_design.icon.material_call_split_icon import MaterialcallSplitIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallSplitIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallSplitIcon = MaterialcallSplitIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
