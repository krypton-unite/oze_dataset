from oze_dataset.dataset import OzeEvaluationDataset, OzeNPZDataset
from oze_dataset import npz_check
from pathlib import Path
from oze_dataset import labels, TIME_SERIES_LENGTH

def test_download(user_name, user_password):
    credentials = {
        'user_name': user_name,
        'user_password': user_password
    }
    npz_check(credentials=credentials)

def test_already_downloaded(user_name, user_password):
    credentials = {
        'user_name': user_name,
        'user_password': user_password
    }
    npz_check(credentials=credentials)

def test_OzeEvaluation(user_name, user_password):
    credentials = {
        'user_name': user_name,
        'user_password': user_password
    }
    dataset_x_path = npz_check(credentials=credentials)
    dataset_eval = OzeEvaluationDataset(
        Path(dataset_x_path.parent, 'x_test_QK7dVsy.csv'),
        TIME_SERIES_LENGTH, given_labels=labels)
    assert dataset_eval.get_x_shape() == (500, 672, 37)

def test_OzeNPZDataset(user_name, user_password):
    credentials = {
        'user_name': user_name,
        'user_password': user_password
    }
    ond = OzeNPZDataset(npz_check(credentials=credentials))
    assert ond.get_x_shape() == (7500, 672, 37)