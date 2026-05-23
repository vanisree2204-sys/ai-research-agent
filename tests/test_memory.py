import json
import os

MEMORY_FILE = "sessions.json"


def test_memory_file_exists():

    assert os.path.exists(MEMORY_FILE)


def test_memory_is_dictionary():

    with open(MEMORY_FILE, "r") as file:

        data = json.load(file)

    assert isinstance(data, dict)