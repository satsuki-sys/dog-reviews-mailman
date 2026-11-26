"""The Dog Reviews the Mailman — entry program.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local runs).
Stdlib only.
"""

import os

ENTRY = (
    "One star. He visits my house every single day and has never once "
    "brought me anything \u2014 the letters aren't even addressed to me."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
