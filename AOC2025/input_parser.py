from typing import List


def get_input_as_lines(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.read().split("\n")]

def get_input_as_lines_without_strip(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line for line in f.read().split("\n")]

def get_input_as_str(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()


def get_input_as_int_matrix(filename: str) -> List[List[int]]:
    lines = get_input_as_lines(filename)
    return [[int(x) for x in line.split(" ")] for line in lines]


def get_input_as_digit_matrix(filename: str) -> List[List[int]]:
    lines = get_input_as_lines(filename)
    return [[int(x) for x in line] for line in lines]


def get_input_as_str_matrix(filename: str) -> List[List[str]]:
    lines = get_input_as_lines(filename)
    return [[char for char in line] for line in lines]