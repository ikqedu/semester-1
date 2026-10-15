# Worksheet 1.3: Task 1
import logging

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

L = int(input("Length of sequence: "))  # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
def gen_recaman(length: int) -> list[int]:
    if length < 0:
        raise ValueError("L must be > 0")

    seq = [0]
    for i in range(1, length):
        next_val_minus = seq[i - 1] - i

        if next_val_minus > 0 and next_val_minus not in seq:
            seq.append(next_val_minus)
        else:
            seq.append(next_val_minus + 2 * i)

        logger.info(f"i: {i}, seq[-1]: {seq[-1]}")

    return seq


def test_gen_recaman() -> None:
    """Test first 10."""

    first_ten_seq = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21]
    gen_recaman_output = gen_recaman(10)

    assert gen_recaman_output == first_ten_seq, (
        f"Does not match 10 test!\nOutput:  {gen_recaman_output}\nExpected:{first_ten_seq}"
    )


test_gen_recaman()
sequence = gen_recaman(L)

# You may wish to use further output for testing purposes while you develop your code

[
    print(item) for item in sequence
]  # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
