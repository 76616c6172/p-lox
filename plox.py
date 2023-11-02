#!/usr/bin/env python3
import sys, pathlib
from typing import List


def run(file_content: str) -> None:
    pass


def runFile(path: str) -> None:
    file_content = pathlib.Path(path).read_text()
    run(file_content)
    pass


def runPrompt() -> None:
    while True:
        try:
            line = input("> ")
            run(line)
        except EOFError:
            print()
            break


def main(args: List[str]) -> None:
    if len(args) > 1:
        print("Usage: plox [script]")
        sys.exit(64)
    elif len(args) == 1:
        runFile(args[0])
    else:
        runPrompt()


if __name__ == "__main__":
    main(sys.argv[1:])
