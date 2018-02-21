from typing import List

def get_file_lines(path: str) -> List[str]:
    input_file = open(path, 'r')
    lines = input_file.readlines()
    input_file.close()

    return lines