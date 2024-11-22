# Pexels Image Scraper (parser_pexels_com)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-WIP-orange.svg)](#)
[![License](https://img.shields.io/badge/license-See%20REPO-lightgrey.svg)](#)


## Project description

Pexels Image Scraper is a lightweight Python utility that automates searching and collecting image links from Pexels.com and optionally downloading them. The project uses Selenium WebDriver (Firefox/GeckoDriver) to navigate Pexels, collects image page links, and provides helper utilities to store and post-process the results. It includes utilities for managing a custom USER_AGENT via a small config helper.


## Tech stack

- Python: 3.8+
- Key libraries:
  - selenium
  - python-dotenv
- Requirements / external tools:
  - Firefox browser
  - GeckoDriver (GeckoDriver/geckodriver.exe is referenced in code — adjust path to local platform)
- Standard library usage: os, time, random, etc.

---

## Quick start — detailed installation

Open a terminal and follow the steps below. Replace values where appropriate.

1. Clone repository (if not already cloned)
```bash
git clone https://github.com/mihaiapostol14/parser_pexels_com.git
cd parser_pexels_com
```

2. Create and Activate a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. GeckoDriver and Firefox

- Install Firefox for your platform.
- Download GeckoDriver and place it in `GeckoDriver/` (or update the path used in code: `Service(executable_path='GeckoDriver/geckodriver.exe')`).
- Ensure the GeckoDriver binary is executable and matches your Firefox version.

---

## Usage

- Create the `config/.env` with your USER_AGENT:
```bash
python setup_private.py
```

- Search for and parse images by providing a query:

Run the main search parser (interactive):
```bash
python main_parser.py
# Example prompt: typing your image please: car
```

- Iterate over a list of image page links and extract images (file-driven mode):
```bash
python parser_image_link.py
# The parser can be pointed at a text file with links (see parser_image_link.ParserItemInfo)
```



Notes:
- The scripts open Firefox via Selenium; do not close the terminal while scripts run.
- Adjust `GeckoDriver` path in code if you placed the driver elsewhere.
- Output directories and files are created by helper utilities in the repository.

---

## Project structure

A concise tree of the repository (representative):
```
parser_pexels_com/
├─ config/
│  ├─ __init__.py   # exposes USER_AGENT
│  └─ load.py       # loads config/.env via python-dotenv
├─ helper/
│  ├─ __init__.py   # Helper, DriverHelper, ElementChecker, image_downloader exports
│  ├─ helper.py     # filesystem helpers, create/remove files, pauses
│  ├─ driver_helper.py
│  ├─ element_checker.py
│  └─ image_downloader.py
├─ GeckoDriver/     # (expected location for geckodriver binary; update as needed)
├─ main_parser.py   # primary entry: MainParser
├─ parser_image_link.py  # iterate by item (read urls file), fetch images
├─ setup_private.py # simple helper to create config/.env (USER_AGENT)
├─ test.py          # small helper/test snippet
└─ README.md
```

---

## Behavior and features

- Search automation: enter keywords, script navigates Pexels search pages.
- Image link collection: collects links and writes them to files.
- Image downloading: helper exists to download images given a link list.
- Custom user agent: avoids simple bot detection by overriding USER_AGENT.
- Element checks & randomized pauses: basic heuristics to avoid detection.

---

## Tips and troubleshooting

- If Selenium throws a WebDriver exception, verify GeckoDriver path and compatibility.
- Ensure `config/.env` contains a valid `USER_AGENT`. Use `python setup_private.py` to create it.
- If a site layout changes, some XPath/class selectors may need updating (check ElementChecker and element queries).
- Consider running Firefox in headless mode by adding options in the parser if you prefer no UI.

---

## Contributing

Contributions are welcome. Suggested small improvements:
- Add a proper requirements.txt with pinned versions.
- Add command-line arguments to the main scripts (to avoid interactive prompts).
- Add retries, better logging, and more robust selector strategies.

---

## License

See repository for license details (not specified in this README).

---

## Author

[Mihai Apostol](https://github.com/mihaiapostol14)