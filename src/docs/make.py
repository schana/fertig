import pathlib
import shutil
import subprocess

import fertig


def main() -> None:
    shutil.rmtree("build", ignore_errors=True)
    build_docs()


def build_docs() -> None:
    fertig_path = str(pathlib.Path(fertig.__file__).resolve().parent)
    subprocess.run(
        [
            "sphinx-apidoc",
            "--separate",
            "--module-first",
            "--force",
            "--no-toc",
            "--implicit-namespaces",
            "-o",
            "build/modules",
            fertig_path,
        ]
    )
    subprocess.run(["sphinx-build", "-b", "html", ".", "build"])
    shutil.rmtree("build/modules", ignore_errors=True)


if __name__ == "__main__":
    main()
