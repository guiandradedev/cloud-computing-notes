import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent


def process_file(path):
    path = Path(path)

    if not path.is_absolute():
        path = PROJECT_ROOT / path

    if path.suffix == "":
        path = path.with_suffix(".md")

    content = path.read_text(encoding="utf-8")

    pattern = r'@import\s+["\'](.+?)["\']'

    def replace_import(match):
        imported_path = path.parent / match.group(1)
        return process_file(imported_path)

    content = re.sub(pattern, replace_import, content)

    # Imports are expanded into README.md, whose base directory is the
    # project root. Resolve image paths from their original Markdown file
    # before writing them back relative to that root.
    image_pattern = r'(!\[[^\]]*\]\()((?:\.\.?/)[^\s)]+)'

    def replace_image(match):
        image_path = (path.parent / match.group(2)).resolve()

        try:
            relative_path = image_path.relative_to(PROJECT_ROOT)
        except ValueError:
            return match.group(0)

        return f"{match.group(1)}{relative_path.as_posix()}"

    return re.sub(image_pattern, replace_image, content)

result = process_file("notes/notes.md")

(PROJECT_ROOT / "README.md").write_text(result, encoding="utf-8")
