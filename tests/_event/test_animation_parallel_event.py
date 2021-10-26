from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names


class TestAnimationParallelEvent:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        animation_parallel: ap.AnimationParallel = ap.AnimationParallel(
            animations=[])
        animation_parallel_event: ap.AnimationParallelEvent = \
            ap.AnimationParallelEvent(this=animation_parallel)
        assert animation_parallel_event.this == animation_parallel
        assert animation_parallel_event.variable_name.startswith(
            f'{var_names.ANIMATION_PARALLEL_EVENT}_')
