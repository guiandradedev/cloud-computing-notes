import re
from pathlib import Path

def process_file(path):
    path = Path(path)

    if path.suffix == "":
        path = path.with_suffix(".md")

    content = path.read_text(encoding="utf-8")

    pattern = r'@import\s+["\'](.+?)["\']'

    def replace_import(match):
        imported_path = path.parent / match.group(1)
        return process_file(imported_path)

    return re.sub(pattern, replace_import, content)

result = process_file("notes/notes.md")

Path("README.md").write_text(result, encoding="utf-8")