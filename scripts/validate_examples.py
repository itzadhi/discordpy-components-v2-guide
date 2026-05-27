from pathlib import Path
import py_compile

root = Path("examples/discordpy-bot/src")
files = sorted(root.rglob("*.py"))
if not files:
    raise SystemExit("No Python example files found")

for file in files:
    py_compile.compile(str(file), doraise=True)

print(f"Compiled {len(files)} Python example files.")
