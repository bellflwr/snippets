from collections.abc import Generator
from typing import TextIO


def buffered_read(file: TextIO, bufsize: int = 1024) -> Generator[str, None, None]:
    """Reads a text file, and returns a generator that will read it one character at a
    time, without loading the whole file to memory.

    :param file: A opened file object (such as one from the `open()` function),
    in text mode.
    :type file: TextIO
    :param bufsize: The size of the buffer, defaults to 1024.
    :type bufsize: int, optional
    :yield: The next character.
    :rtype: Generator[str, None, None]
    """
    while buf := file.read(bufsize):
        yield from buf
