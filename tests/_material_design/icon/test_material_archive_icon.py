from apysc._material_design.icon.material_archive_icon import MaterialArchiveIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialArchiveIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialArchiveIcon = MaterialArchiveIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
