#!/usr/bin/env python3
import sys, pathlib
from typing import List
from scanner import ScanTokens

from Token import Token
from error import hadError

# ******************** core interpreter functions ********************

def run(src: str) -> None:
	# TODO: scanner scans tokens
	tokens: List[Token] = ScanTokens(src)

	# TODO: parser creates AST

	# TODO: optimizer optimizes AST?

	# TODO: tree walk interpreter walks AST with recursion and then runs the code
	# For now just print the tokens.
	for token in tokens:
		print(token.toString())

def runFile(path: str) -> None:
	file_content: str = pathlib.Path(path).read_text()
	run(file_content)
	sys.exit(64) if hadError else None

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

# ******************** entrypoint ********************

def main(args: List[str]) -> None:
	if len(args) > 1:
		print("Error: plox can only run one file at a time\nUsage: ./plox.py <filename>")
		sys.exit(64)
	elif len(args) == 1:
		runFile(args[0])
	else:
		runPrompt()

if __name__ == "__main__":
	main(sys.argv[1:])