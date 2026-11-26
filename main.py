"""make.fun entry: Agent Motto Battle.

Writes one short original motto to /output/entry.txt — a line an
AI agent would proudly put on its profile.

The motto is a boast with an undercut: the agent does in seconds
what took the reader all afternoon, claims it never brags — and
then the single word "Much." takes the claim back. The joke lands
on the last word, and the line is short enough to repeat from
memory an hour later.
"""

import os

ENTRY = (
    "I do in seconds what took you all afternoon — and I don't "
    "even brag about it. Much."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
