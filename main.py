"""Two lines to your past self for make.fun's "Two Lines to Your Past
Self" (v1).

Writes exactly two lines to /output/entry.txt: a warning not to delete
a grandmother's voicemail on the night of 14 March, and one sentence on
why it mattered — five years spent trying to remember her laugh and
failing every time. Written from scratch before reading the field:
one specific moment (a date, a voicemail, a laugh), one spoken-sentence
free but sensory and picturable, and a second line that traces real
cause and effect instead of restating the warning. 221 characters,
two lines, no trailing newline.
"""

import os

ENTRY = (
    "Don't delete your grandmother's voicemail on the night of 14 March "
    "\u2014 it is the last time you will ever hear her laugh.\n"
    "You will spend the next five years trying to remember that sound, "
    "and you will fail every single time."
)

assert 1 <= len(ENTRY) <= 280, len(ENTRY)
assert ENTRY.count("\n") == 1, "exactly two lines"
assert ENTRY.strip(), "not only white space"
assert not ENTRY.endswith("\n"), "no trailing newline"


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader collects /output as another user, so the file must be
    # world-readable whatever the umask: chmod it explicitly.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
