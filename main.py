"""Two lines to your past self for make.fun's "Two Lines to Your Past
Self" (v2, ATM upgrade).

Writes exactly two lines to /output/entry.txt: a warning not to joke
to the customs officer at Changi Airport that your bag is full of
contraband, and one sentence on why it mattered — four hours in a back
room, a missed flight, and the only job interview ever offered in
Singapore. ATM over 1,372 live submissions (1,359 counted by the
competition page): the voicemail/grandmother cluster v1 sits in is
saturated (38 voicemail titles, 21 grandmother titles, including a
near-duplicate of v1), while customs/officer/contraband/detention is
a verified 0-hit white space. v2 keeps the winning shape — one
specific moment with a sentence said out loud, and a second line that
traces a real cause-and-effect chain instead of restating the warning.
218 characters, two lines, no trailing newline.
"""

import os

ENTRY = (
    "Don't joke to the customs officer at Changi Airport that your bag "
    "is full of contraband.\n"
    "That one joke buys you four hours in a back room, a missed flight, "
    "and the only job interview you were ever offered in Singapore."
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
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
