# ******************** error handling ********************

hadError: bool = False

def Report(line: int, msg: str, where: str) -> None:
	print(f"[line {line}] Error {where}: {msg}")
	global hadError
	hadError = True

def Error(line: int, msg: str) -> None:
	Report(line, "", msg)
