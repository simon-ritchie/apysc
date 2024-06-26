from apysc._material_design.icon.material_settings_input_component_outlined_icon import (  # noqa
    MaterialSettingsInputComponentOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsInputComponentOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsInputComponentOutlinedIcon = (
            MaterialSettingsInputComponentOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
