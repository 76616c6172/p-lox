#!/usr/bin/env python3
import sys, pathlib
from typing import List

hadError: bool = False


# ******************** error handling ********************


def report(line: int, where, msg: str) -> None:
    print(f"[line {line}] Error {where}: {msg}")

    global hadError
    hadError = True


def error(line: int, msg: str) -> None:
    report(line, "", msg)


# ******************** core interpreter functions ********************


def run(src: str) -> None:
    # "scan" tokens here
    tokens: list[str] = src.split()

    # For now just print the tokens.
    for token in tokens:
        print(token)


def runFile(path: str) -> None:
    file_content = pathlib.Path(path).read_text()
    run(file_content)

    if hadError:
        sys.exit(64)


def runPrompt() -> None:
    global hadError

    while True:
        try:
            line = input("> ")
            run(line)
            hadError = False
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
