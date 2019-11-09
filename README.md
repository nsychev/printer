# Printer

Simple remote print server for ICPC-like onsite contests. Consists of two parts: server — Flask web application to accept jobs and generate tasks, and worker — Python console application for Windows, which downloads new tasks and sends them to printer.

## Server side

Requirements: Python 3.6+, PDFLaTeX.

1. Adjust `config.sample.py` to your needs and rename it to `config.py`.

2. Install dependencies: `pip install -r requirements.txt`.

3. Run application: `python3 app.py`.

## Client side

Requirements: Python 3.6+.

1. Adjust `config.sample.py` to your needs and rename it to `config.py`.

2. Fetch binary dependencies: [PDFToPrinter.exe](http://www.columbia.edu/~em36/pdftoprinter.html) and install Python ones: `pip install -r requirements.txt`

3. Run agent: `py.exe -3 agent.py`.

## License

[MIT](LICENSE)
