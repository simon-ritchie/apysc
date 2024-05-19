from apysc._material_design.icon.material_forward_to_inbox_outlined_icon import MaterialforwardToInboxOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforwardToInboxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialforwardToInboxOutlinedIcon = MaterialforwardToInboxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
