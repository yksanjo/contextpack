#!/usr/bin/env python3
import argparse
import json
import pathlib
import tarfile


def main() -> int:
    parser = argparse.ArgumentParser(description="Bundle context files for agent runs")
    parser.add_argument("--name", default="contextpack")
    parser.add_argument("--output", default=".")
    parser.add_argument("files", nargs="+")
    ns = parser.parse_args()

    output_dir = pathlib.Path(ns.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{ns.name}.tar.gz"

    added = []
    with tarfile.open(archive, "w:gz") as tar:
        for fp in ns.files:
            path = pathlib.Path(fp)
            if path.exists():
                tar.add(path, arcname=path.name)
                added.append(str(path))

    print(json.dumps({"archive": str(archive), "files_added": added}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
