# Oze dataset

[![PyPI version](https://badge.fury.io/py/oze-dataset.svg)](https://badge.fury.io/py/oze-dataset) [![travis](https://travis-ci.org/krypton-unite/oze-dataset.svg?branch=master)](https://travis-ci.org/github/krypton-unite/oze-dataset) [![codecov](https://codecov.io/gh/krypton-unite/oze-dataset/branch/master/graph/badge.svg)](https://codecov.io/gh/krypton-unite/oze-dataset) [![GitHub license](https://img.shields.io/github/license/krypton-unite/oze_dataset)](https://github.com/krypton-unite/oze_dataset)

## Description
Downloads datasets files from https://challengedata.ens.fr/participants/challenges/28/ and create npz file from them.

## Installation

```terminal
pip install oze-dataset
```

## Usage

```python
from oze_dataset import npz_check

if __name__ == "__main__":
    credentials = {
        'user_name': 'your_user_name',
        'user_password': 'your_user_password'
    }
    npz_check(credentials=credentials)
```