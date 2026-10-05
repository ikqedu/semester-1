"""
Utility functions for Worksheet 1.2.
"""
from pathlib import Path
import argparse


def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers


def read_file() -> list[float]:
    """
    Read list of floats from file specified as positional argument.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")  # positional
    args = parser.parse_args()
    
    with Path(args.filename).open(mode="r") as f:
        return [float(line.strip()) for line in f.readlines() if line.strip()]

