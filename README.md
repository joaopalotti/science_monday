science_monday
==============================

An example of how to use some python data science tools for my science monday presentation

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


Jupyter Book Updates
==============================

Steps to get Jupyer book up and running at: https://joaopalotti.github.io/science_monday/:

- Renamed the original ``docs`` from the cookiecutter data science template as ``cookie_cutter_docs/``. It could also be removed.
- The folder ``my_jupyter_book/`` was created using the Jupyer Notebook cookie_cutter command:
    ```shel
    jupyter-book create my_jupyter_book/ --cookiecutter
    ```
   See <a target="_blank" href="https://jupyterbook.org/start/overview.html/"> Jupyter Book documentation</a> for alternative options. 
  
- Built the notebook with:
 ```shell
 cd my_jupyter_book/science_monday_book
 jupyter-book build science_monday_book
 ```
        
- Installed ghp-import (``pip install ghp-import``) and used it:
  ```shell
  ghp-import -n -p -f my_jupyter_book/science_monday_book/science_monday_book/_build/html
  ```
- <a target="_blank" href="https://jupyterbook.org/publish/gh-pages.html">Published it</a>.

