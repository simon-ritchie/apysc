from apysc._material_design.icon.material_restore_from_trash_outlined_icon import (
    MaterialRestoreFromTrashOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRestoreFromTrashOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRestoreFromTrashOutlinedIcon = (
            MaterialRestoreFromTrashOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
