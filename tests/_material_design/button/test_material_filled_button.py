from typing import List
from apysc._expression import var_names
from apysc._material_design.button.material_filled_button import MaterialFilledButton
from apysc._material_design.icon.material_chat_icon import MaterialChatIcon
from apysc._material_design.icon.material_home_icon import MaterialHomeIcon
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestMaterialFilledButton:
    @apply_test_settings()
    def test___init__(self) -> None:
        label: str = "Test Label"
        prefix_icon: MaterialHomeIcon = MaterialHomeIcon()
        suffix_icon: MaterialChatIcon = MaterialChatIcon()
        x: float = 100
        y: float = 200
        font_family: List[str] = ["Arial", "Helvetica"]
        font_size: int = 20
        parent: ap.Sprite = ap.Sprite()
        button: ap.MaterialFilledButton = ap.MaterialFilledButton(
            label=label,
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon,
            x=x,
            y=y,
            text_color=ap.Colors.RED_BROWN_622F22,
            font_family=font_family,
            font_size=font_size,
            background_color=ap.Colors.GRAY_777777,
            parent=parent,
            variable_name_suffix="test_button",
        )
        assert button._label == ap.String(label)
        assert button._label_text.text == ap.String(label)
        assert button.parent == parent
        assert var_names.MATERIAL_FILLED_BUTTON in button._variable_name
        assert button._variable_name_suffix == 'test_button'

    @apply_test_settings()
    def test__redraw_background(self) -> None:
        button: ap.MaterialFilledButton = ap.MaterialFilledButton(
            label="Test label",
            prefix_icon=MaterialHomeIcon(),
            suffix_icon=MaterialChatIcon(),
            variable_name_suffix="test_button",
        )
        rectangle_child_exists: bool = False
        for child in button.graphics._children._value:
            if isinstance(child, ap.Rectangle):
                rectangle_child_exists = True
                assert child.ellipse_width != ap.Int(0)
                assert child.ellipse_height != ap.Int(0)
                break
        assert rectangle_child_exists
