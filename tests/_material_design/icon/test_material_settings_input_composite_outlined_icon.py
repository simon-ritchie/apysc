from apysc._material_design.icon.material_settings_input_composite_outlined_icon import (  # noqa
    MaterialSettingsInputCompositeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsInputCompositeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsInputCompositeOutlinedIcon = (
            MaterialSettingsInputCompositeOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
