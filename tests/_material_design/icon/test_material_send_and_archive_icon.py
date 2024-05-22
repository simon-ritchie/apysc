from apysc._material_design.icon.material_send_and_archive_icon import (
    MaterialSendAndArchiveIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSendAndArchiveIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSendAndArchiveIcon = MaterialSendAndArchiveIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
