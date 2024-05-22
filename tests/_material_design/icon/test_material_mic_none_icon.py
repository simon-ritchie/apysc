from apysc._material_design.icon.material_mic_none_icon import MaterialMicNoneIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMicNoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMicNoneIcon = MaterialMicNoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
