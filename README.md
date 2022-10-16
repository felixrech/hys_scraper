# 'Have your Say' scraper

![Python version](https://img.shields.io/badge/python-%3E%3D3.6-blue?logo=python) [![PyPI version](https://badge.fury.io/py/hys_scraper.svg)](https://badge.fury.io/py/hys_scraper) [![GPLv3 license](https://img.shields.io/github/license/felixrech/hys_scraper)](https://github.com/felixrech/hys_scraper/blob/master/LICENSE)

A small utility to scrape the European Commission's 'Have your Say' plattform ([https://ec.europa.eu/info/law/better-regulation/have-your-say](https://ec.europa.eu/info/law/better-regulation/have-your-say)). Can scrape an initiative's feedback submissions, attachments of these submissions, and the by country and by category statistics.

## Installation

```bash
pip3 install hys_scraper
```

Tested to work with Python 3.9 on a Linux machine and Google Colab notebooks.

## Getting started

To get started, you will need the publication id of the initiative you want to scrape. To get this, simply navigate to the initiative on 'Have your Say' and look at the URL - the number at the end is the publication id you will use in the next step. For example, for the [AIAct commission adoption initiative](https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/12527-Artificial-intelligence-ethical-and-legal-requirements/feedback_en?p_id=24212003), the publication id would be `24212003`.

To scrape an initiative the following is sufficient (replace `24212003` with the publication id of the initiative you want to scrape):

```bash
python3 -m hys_scraper 24212003
```

This will create a new folder in your current working directory with the following layout:

```
24212003_requirements_for_artificial_intelligence/
├── attachments
│   ├── 2488672.pdf
│   ├── 2596917.pdf
│   └── ...
├── attachments.csv
├── categories.csv
├── countries.csv
└── feedbacks.csv

1 directory, 263 files
```

## Advanced usage

The command line interface has a few more arguments. For example instead of having `hys_scraper` create a folder in the local working directory to save results into, you can also manually specify a target directory.

```
$ python3 -m hys_scraper -h
Scrape feedback and statistics from the European Commission's 'Have your Say' plattform.

positional arguments:
  PID                   The publication id - what comes after 'p_id=' in the initiative's URL.

optional arguments:
  -h, --help            show this help message and exit
  --dir target_dir, --target_dir target_dir
                        Directory to save the feedback and statistics dataframes to. Defaults to creating a new
                        folder in the current working directory.
  --no_attachments      Whether to skip the download of attachments.
  --sleep_time t        Minimum time between consecutive HTTP requests (in seconds).
```

Alternatively, you can also access `hys_scraper` from Python:

```python
from hys_scraper import HYS_Scraper
feedbacks, countries, categories = HYS_Scraper("24212003").scrape()
```

Similar options are available as for the command line interface, check out `help(HYS_Scraper)` for details.
