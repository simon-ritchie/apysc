from apysc._material_design.icon.material_restore_from_trash_icon import (
    MaterialrestoreFromTrashIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrestoreFromTrashIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrestoreFromTrashIcon = MaterialrestoreFromTrashIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
