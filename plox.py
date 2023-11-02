#!/usr/bin/env python3
import sys
from typing import List


def runFile(file_path: str) -> None:
    pass


def runPrompt() -> None:
    pass


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
