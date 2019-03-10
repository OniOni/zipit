import argparse
import os
import pathlib
import shutil
import tempfile
import zipapp

MAGIC_MAIN = """
import sys
import runpy

if __name__ == '__main__':
    sys.path.insert(1, f'{sys.path[0]}/deps')
    runpy.run_module('mod', run_name='__main__')
"""


def setup() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('-d', '--deps')

    return parser


def build_app(src: str, deps: str = None):
    tmpdir = tempfile.mkdtemp(suffix='.zipit')

    os.mkdir(f"{tmpdir}/app")
    shutil.copytree(src, f"{tmpdir}/app/mod")
    if deps:
        shutil.copytree(deps, f"{tmpdir}/app/deps")

    magic_main = pathlib.Path(f"{tmpdir}/app/__main__.py")
    magic_main.touch()
    magic_main.write_text(MAGIC_MAIN)

    zipapp.create_archive(f"{tmpdir}/app", target="app.pyz")
    shutil.rmtree(tmpdir)

def main():
    parser = setup()
    args = parser.parse_args()

    build_app(
        src=args.src,
        deps=args.deps
    )


if __name__ == '__main__':
    main()
