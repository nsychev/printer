import datetime
import os
import subprocess
import sys
import tempfile
import threading
import uuid

import config


def run(username, source):
    with open('template.tex') as f:
        template = f.read()
    template = template.replace('%USER%', username).replace('%DATE%', str(datetime.datetime.now()))

    with tempfile.TemporaryDirectory() as base_path:
        with open(os.path.join(base_path, 'main.tex'), 'w') as f:
            f.write(template)
        with open(os.path.join(base_path, 'source.txt'), 'w') as f:
            f.write(source)

        subprocess.run(
            ['pdflatex', 'main.tex'],
            cwd=base_path
        )

        result_filename = f"{uuid.uuid4()}.pdf"
        os.rename(
            os.path.join(base_path, 'main.pdf'),
            os.path.join("static/pdfs", result_filename)
        )
        print(f"Created file {result_filename}", file=sys.stderr, flush=True)


def run_threaded(username, source):
    threading.Thread(target=run, args=(username, source)).start()
