from oze_dataset.utils import npz_check
from pathlib import Path

def test_download(user_name, user_password):
    credentials = {
        'user_name': user_name,
        'user_password': user_password
    }
    npz_check(Path('datasets'), 'dataset', credentials=credentials)
