from apysc._material_design.icon.material_restore_from_trash_icon import (
    MaterialRestoreFromTrashIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRestoreFromTrashIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRestoreFromTrashIcon = MaterialRestoreFromTrashIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
