# Private Jet Emissions

This is an example Observable Framework project that uses a python data loader to load and transform data from an S3 bucket before visualizing using Javascript and Markdown.

## Data loader

The Python [data loader](../../docs/loaders.md) `predictions.csv.py` reads in the `penguins.csv` file, then performs logistic regression using scikit-learn's [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) function.

## Charts

All charts are drawn with [Observable Plot](https://observablehq/com/plot).

## Reuse this example

Copy the contents of the `penguins-classification` directory into a new Observable Framework project. Then, run the following set up steps (as needed) get started:

- If needed, install python3
- Create and activate a virtual environment
  - `$ python3 -m venv .venv`
  - `$ source .venv/bin/activate`
- Pip install modules from requirements.txt
  - `$ pip install -r requirements.txt`
- Run and preview the page
  - `$ yarn`
  - `$ yarn dev`
- Make changes to the page (`index.md`) or data loader and save to see instant updates in the [live preview](https://observablehq.com/framework/getting-started#test-live-preview)

[Learn more about deploying with Github actions](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#requirements-file) for Python 3.6 & `requirements.txt`.
