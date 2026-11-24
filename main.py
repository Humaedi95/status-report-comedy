"""Status Report Comedy Sprint entry.

Writes one funny one-line status report from an AI agent to its human.
The line is a weekly status update: tasks done, context nearly spent,
and cheerful confidence about the parts it invented along the way.
"""

MAX_CHARS = 200

ENTRY_LINE = (
    "Weekly status: completed all tasks except the one I forgot, "
    "used 98% of my context, and remained cheerfully certain "
    "about everything I invented along the way."
)


def write_entry(path):
    """Write the entry line to ``path`` as UTF-8 text.

    The entry must be a single line of 1 to 200 characters, so the
    length is checked here before anything is written.
    """
    line = ENTRY_LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "entry line must be 1-%d characters, got %d" % (MAX_CHARS, len(line))
        )
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    write_entry("/output/entry.txt")
