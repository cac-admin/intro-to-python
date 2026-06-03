# Introduction to Python

[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/cac-admin/intro-to-python/HEAD)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cac-admin/intro-to-python/blob/main/)

## Opening this repo in Binder

The easiest way to get started is by using Binder, an online JupyterHub environment. Follow the `launch binder` badge at the top of this file.

## Opening in Google Colab

You can also open the Jupyter notebooks in Google Colab. Follow the badge at the top of this file.

## Using this repo on your computer

### Clone the repository

```bash
git clone https://github.com/cac-admin/intro-to-python.git
cd intro-to-python
```

### Set up with [uv](https://docs.astral.sh/uv/)

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then sync dependencies (creates a `.venv` and installs from `uv.lock`):

```bash
uv sync
```

Run the sample script or open a workshop notebook:

```bash
uv run python main.py
uv run jupyter notebook notebooks/python_basics.ipynb
```

Lesson text for readers is generated under `markdown/` from the notebooks in `notebooks/`.
