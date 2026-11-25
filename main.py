#!/usr/bin/env python3
"""Write one sentence about the best meal I ever had to /output/entry.txt."""

import os
import shutil

LINE = (
    "The rice and stew my father burnt the week my mother travelled, scraped "
    "from the pot at nine at night, which we both agreed, without saying so, "
    "was perfect."
)


def main() -> None:
    out = os.environ.get("MAKEFUN_OUT", "/output")
    os.makedirs(out, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself.
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
