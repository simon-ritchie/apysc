import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestAddToParentMixIn:
    @apply_test_settings()
    def test__add_to_parent(self) -> None:
        stage: ap.Stage = ap.Stage()
        circle: ap.Circle = ap.Circle(
            x=50,
            y=50,
            radius=50,
        )
        circle._add_to_parent(parent=None)
        assert circle.parent == stage

        sprite: ap.Sprite = ap.Sprite()
        circle = ap.Circle(
            x=50,
            y=50,
            radius=50,
        )
        circle._add_to_parent(parent=sprite)
        assert circle.parent == sprite
