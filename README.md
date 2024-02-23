# Private Jet Emissions

This is a data visualization of a dataset of 17k private jet flights from 200 people in 2023 that I collected using the OpenSky API.

It demonstrates the use of the new Observable 2.0 Framework. This project uses a python data loader to load and transform data from an S3 bucket before visualizing using Javascript and Markdown.

This is a significant advantage over the old way of doing the analysis in a separate repo, pushing to S3, then either downloading and uploading to observable or setting up a separate frontend to display the data.

## Data loader

This is the coolest part of Observable Framework. You can do your analysis in any language (I prefer Python) and the frontend will hot reload with the changes when the analysis re-runs, without having to even re-load the page!

The Python data loaders, [for example, aircrafts, ](../../docs/loaders.md) `flights.csv.py` loads data from S3, summarizes it, and writes it to .csv files.

## Charts

All charts are drawn with [Observable Plot](https://observablehq/com/plot).

Tables are produced using Observable's native `Inputs.table()` function, which is an extremely powerful one-liner for making a performant table out of JSON data.

You can also use D3 for custom charts!

## Deployment

After running `yarn build` Observable generates a static site and writes it to the `dist` directory. This can be deployed anywhere.

## Setup

Important: you have to be using node >= 20 for this to work.

Any time you change the config, you have to re-start the server. Otherwise, there's hot reloading - even for the data loaders!

### Install steps

- If needed, install python3
- Create and activate a virtual environment
  - `$ python3 -m venv .venv`
  - `$ source .venv/bin/activate`
- Pip install modules from requirements.txt
  - `$ pip install -r requirements.txt`
- Run and preview the page
  - `$ yarn`
  - `$ yarn dev`
- Make changes to the page (`index.md`) or data loader and save.
