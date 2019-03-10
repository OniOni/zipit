import os
import pathlib
import shutil
import tempfile
from typing import List
import zipapp

MAGIC_MAIN = """
import sys
import runpy

if __name__ == '__main__':
    sys.path.insert(1, f'{sys.path[0]}/deps')
    runpy.run_module('mod', run_name='__main__')
"""


def build_app(src: str, deps: List[str] = None, output: str = None):
    tmpdir = tempfile.mkdtemp(suffix='.zipit')

    os.mkdir(f"{tmpdir}/app")
    shutil.copytree(src, f"{tmpdir}/app/mod")
    if deps:
        for d in deps:
            shutil.copytree(d, f"{tmpdir}/app/deps")

    magic_main = pathlib.Path(f"{tmpdir}/app/__main__.py")
    magic_main.touch()
    magic_main.write_text(MAGIC_MAIN)

    if not output:
        output = 'app.pyz'

    zipapp.create_archive(f"{tmpdir}/app", target=output)
    shutil.rmtree(tmpdir)
