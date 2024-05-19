from apysc._material_design.icon.material_markunread_mailbox_icon import (
    MaterialmarkunreadMailboxIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmarkunreadMailboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmarkunreadMailboxIcon = MaterialmarkunreadMailboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
