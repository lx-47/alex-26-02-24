
# Suggested code improvements

import os
import logging
from typing import List, Dict, Union

# Define constants at the top of the file
FILE_EXTENSION = ".txt"
LOG_FILE = "log.txt"

# Add docstrings for functions and classes
def get_file_paths(directory: str) -> List[str]:
    """
    Returns a list of file paths in the given directory with the specified file extension.
    """
    file_paths = []
    for file in os.listdir(directory):
        if file.endswith(FILE_EXTENSION):
            file_paths.append(os.path.join(directory, file))
    return file_paths

def get_file_contents(file_paths: List[str]) -> List[str]:
    """
    Returns a list of file contents for the given file paths.
    """
    file_contents = []
    for file_path in file_paths:
        with open(file_path, "r") as file:
            file_contents.append(file.read())
    return file_contents

def process_file(file_content: str) -> Dict[str, Union[int, float]]:
    """
    Processes the given file content and returns a dictionary of word counts and average word length.
    """
    word_count = 0
    total_length = 0.0
    word_dict = {}

    for word in file_content.split():
        word_count += 1
        total_length += len(word)
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return {
        "word_count": word_count,
        "average_word_length": total_length / word_count,
        "word_distribution": word_dict,
    }

def write_to_log(log_message: str):
    """
    Writes the given log message to a file.
    """
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_message + "\n")

def main():
    """
    Main function that processes a directory of text files and writes the results to a log file.
    """
    directory = input("Enter the directory path: ")

    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    file_paths = get_file_paths(directory)
    file_contents = get_file_contents(file_paths)

    for file_content in file_contents:
        processed_data = process_file(file_content)
        write_to_log(str(processed_data))

if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
    main()