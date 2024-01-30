#!/usr/bin/env python3
import sys, pathlib
from typing import List
from scanner import ScanTokens

from Token import Token

hadError: bool = False

# ******************** error handling ********************

def report(line: int, msg, where: str) -> None:
	print(f"[line {line}] Error {where}: {msg}")
	global hadError
	hadError = True

def error(line: int, msg: str) -> None:
	report(line, "", msg)

# ******************** core interpreter functions ********************

def run(src: str) -> None:
	# TODO: implement lexical grammar to actually emit tokens
	tokens: List[Token] = ScanTokens(src)

	# For now just print the tokens.
	for token in tokens:
		print(token)
		# print(token.toString())

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