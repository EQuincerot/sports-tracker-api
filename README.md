# sports-tracker-api
Python API to download GPX files from https://www.sports-tracker.com using Chrome browser.
This is far from complete or ideal, it is a minimum viable product which did the job for me. Tested on Macbook.

## Prerequisities

- Chrome installed
- ChromeDriver downloaded and unzipped to *dir*

## How to use

1. Save `data/secrets_template.yaml` as `data/secrets.yaml`.
1. Edit `data/secrets.yaml` and provide your sports-tracker username and password.
1. Open your terminal and set you current directory to the root of this repo (after `ls` should see directories `data` and `examples`.
1. Run `python examples/download_all_workouts_as_gpx.py`.

You should see Chrome browser opening, login to sports-tracker and save your workouts as `*.gpx` files into the default downloads directory (e.g. `~/Downloads`). 
The file names are automatic and follow the pattern `MM_DD_YY HH_NN.gpx`, where `MM` is month, `DD` is day in month, `YY` is the last two digits of the year, `HH` is hour and `NN` is minute of the workout start. This is default naming convention by sports-tracker.

