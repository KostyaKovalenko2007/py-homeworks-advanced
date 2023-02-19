import unittest
from ya_disk import YaDisk
import requests
class TestYaDisk(unittest.TestCase):
    def test_responce(self):
        yaDsk = YaDisk()
        resp = yaDsk.creade_folder()
        yaDsk.creade_folder()
        self.assertIn(resp,[201,],"Folder creation response is not in expected statuses")

    def test_folder_in_list(self):
        yaDsk = YaDisk()
        resp = yaDsk.creade_folder()
        token = 'y0_AgAAAAAH-cyMAADLWwAAAADWcsIdSNINDf8GTwOlO_SCG-DPRmc-qTU'
        base_url = 'https://cloud-api.yandex.net/v1/disk'
        session = requests.session()
        session.headers = {'Accept': 'application/json',
                                'Authorization': 'OAuth ' + token}
        folder_list = session.get(f'{base_url}/resources?path=/')
        if folder_list.status_code == 200:
            exists = False
            for item in  folder_list.json().get('_embedded').get('items'):
                if item.get('name') == 'foo':
                    exists = True
                    break
            yaDsk.delete_folder()
            self.assertEqual(exists, True, 'Folder not created because not found in folder list')









