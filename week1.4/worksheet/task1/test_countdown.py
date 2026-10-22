from .countdown import countdown
import pytest
import random

def test_countdown(capsys) -> None:
    
    def _check_countdown(num: int) -> None:
        countdown(num)
        out, err = capsys.readouterr()

        # Countdown includes num
        expt_count = '\n'.join(str(i) for i in range(num, -1, -1)) + '\n'
        assert out == expt_count

    for _ in range(10):
        num = random.randint(10, 100)
        _check_countdown(num)

