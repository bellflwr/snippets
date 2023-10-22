from typing import TextIO
from collections.abc import Generator

# Reads a text file, and returns a generator that will read it one character at a time,
# without loading the whole file to memory
def buffered_read(file: TextIO, bufsize: int = 1024) -> Generator[str, None, None]:
    while buf := file.read(bufsize):
        for char in buf:
            yield char
          
