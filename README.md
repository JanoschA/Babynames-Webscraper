# Baby Names Webscraper

This Python-based project is a webscraper that extracts the most popular baby names from the [Hipp site](https://www.hipp.de/schwanger/ratgeber/babynamen/top-200-vornamen/).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Content Example](#content-example)
- [License](#license)

## Features

This project is designed with the capability to extract the top 200 names for both girls and boys from the [Hipp site](https://www.hipp.de/schwanger/ratgeber/babynamen/top-200-vornamen/). The extracted names are then efficiently stored in a CSV file named `names.csv`, providing an easy and convenient way to access and analyze the data.

## Installation

1. Ensure Python is installed on your system.
2. Clone this repository.

## Usage

Run the script using the command:

```bash
python3 main.py
```

## Content Example
The following is an example of the content of the CSV file `names.csv`:
```
Position;Girlname;Boyname
1;Emilia;Noah
2;Mia;Leon
3;Emma;Liam
...
```
After running the script, the CSV file will be created in the same directory as the script.

## License
This project is licensed under the MIT License.