import apysc as ap
from apysc._display.use_hand_cursor_mixin import UseHandCursorMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestUseHandCursorMixIn:
    @apply_test_settings()
    def test__initialize_use_hand_cursor(self) -> None:
        mixin: UseHandCursorMixIn = UseHandCursorMixIn()
        mixin._initialize_use_hand_cursor()
        assert mixin._use_hand_cursor == ap.Boolean(False)

        mixin._use_hand_cursor = ap.Boolean(True)
        mixin._initialize_use_hand_cursor()
        assert mixin._use_hand_cursor == ap.Boolean(True)

    @apply_test_settings()
    def test_use_hand_cursor(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        use_hand_cursor: ap.Boolean = sprite.use_hand_cursor
        assert use_hand_cursor == ap.False_

        sprite.use_hand_cursor = ap.True_
        assert sprite.use_hand_cursor == ap.True_
        expression: str = expression_data_util.get_current_expression()
        assert "cursor" in expression
        assert "pointer" in expression
        assert "auto" in expression
