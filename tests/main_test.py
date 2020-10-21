from oze_dataset import npz_check

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
