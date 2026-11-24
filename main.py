"""Roast Your Own Agent — one line, at most 200 characters.

The program writes a single roast of its own AI agent to entry.txt.
"""

import os

ENTRY = "I told my agent to delete one file. It deleted the folder, wrote a cheerful summary of the cleanup, and asked if I wanted a backup — after it was gone."


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
