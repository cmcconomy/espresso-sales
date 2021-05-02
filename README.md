# espresso-sales
Python app to collect all sales on espresso equipment in Canada (!)

## Installation

### Virtual Environment
*Optional:* `python3 -m venv .venv` followed by `source .venv/bin/activate`

### Install Requirements
`pip3 install -r requirements.txt`

## Running
*(If you installed a Virtual Environment, ensure you activate it as above)*
`python3 espresso_sales > docs/data/sales.json`

## Daily Update
The real magic here is in the [pipeline](.github/workflows/refresh.yml) which uses a 'cron' schedule to run a new scan every morning to update the 'github.io' doc page.
