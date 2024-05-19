from apysc._material_design.icon.material_restore_from_trash_outlined_icon import (
    MaterialrestoreFromTrashOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrestoreFromTrashOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrestoreFromTrashOutlinedIcon = (
            MaterialrestoreFromTrashOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
