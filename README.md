<p align="center">
  <h3 align="center">PGA TOUR DATA SCRAPER AND DATASETS</h3>

  <p align="center">
    Datasets scraped and collected from <a href="https://www.pgatour.com/stats">PGA Tour Statistics</a>

  </p>
</p>


## Table of contents

- [Status](#status)
- [Implemented Functionalities](#implemented-functionalities)
- [Datasets Overview](#datasets-overview)
- [Python Project Structure](#python-project-structure)

## Status

Actively adding new features for pulling different data for the PGA Tour

## Implemented Functionalities

Pulling... 
- player career profiles
- player stats for seasons from 1987-2024
- player directory
- player years overview
- player achievements

## Datasets Overview

```text
data/
└── players/
└── stats/
```

## Python Project Structure


```text
src/
├── main.py
├── classes/
│   ├── player_stats/
│   │   └── ...
│   ├── players/
│   │   └── ...
│   ├── tour/
│   │   └── ...
│   └── __init__.py
├── helpers/
│   ├── ...
│   └── __init__.py
├── tasks/
│   └── player_tasks/
│       └── ...
tests/
└── test_files
└── ...
```