from apysc._material_design.icon.material_add_to_drive_icon import (
    MaterialAddToDriveIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddToDriveIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddToDriveIcon = MaterialAddToDriveIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
