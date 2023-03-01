import apysc as ap
from apysc._display.svg_text_singleton_for_text_span import SVGTextSingletonForTextSpan
from apysc._testing.testing_helper import apply_test_settings


class TestSVGTextSingletonForTextSpan:
    @apply_test_settings()
    def test_get_instance(self) -> None:
        stage: ap.Stage = ap.Stage()
        instance_1: ap.SVGText = SVGTextSingletonForTextSpan.get_instance()
        assert instance_1.text == ap.String("")
        assert instance_1.visible == ap.Boolean(False)
        assert (
            SVGTextSingletonForTextSpan._stage_id_key_svg_texts[id(stage)] == instance_1
        )

        instance_2: ap.SVGText = SVGTextSingletonForTextSpan.get_instance()
        assert instance_1 == instance_2

        ap.Stage()
        instance_3: ap.SVGText = SVGTextSingletonForTextSpan.get_instance()
        assert instance_1 != instance_3
