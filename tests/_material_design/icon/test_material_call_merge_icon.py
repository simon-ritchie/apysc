from apysc._material_design.icon.material_call_merge_icon import MaterialCallMergeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallMergeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallMergeIcon = MaterialCallMergeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
