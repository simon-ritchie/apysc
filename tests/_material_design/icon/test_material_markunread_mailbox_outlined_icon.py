from apysc._material_design.icon.material_markunread_mailbox_outlined_icon import (
    MaterialMarkunreadMailboxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkunreadMailboxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkunreadMailboxOutlinedIcon = (
            MaterialMarkunreadMailboxOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
