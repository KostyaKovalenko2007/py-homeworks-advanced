import requests
class YaDisk():
    base_url = 'https://cloud-api.yandex.net/v1/disk'
    session = None
    def __init__(self, token='y0_AgAAAAAH-cyMAADLWwAAAADWcsIdSNINDf8GTwOlO_SCG-DPRmc-qTU'):
        self.session = requests.session()
        self.session.headers = {'Accept': 'application/json',
                                'Authorization': 'OAuth ' + token}
        pass
    def creade_folder(self,fldr_name='foo'):
        folder_resp = self.session.put(f'{self.base_url}/resources?path={fldr_name}')
        return folder_resp.status_code
    def delete_folder(self,fldr_name='foo'):
        folder_resp = self.session.delete(f'{self.base_url}/resources?path={fldr_name}')
        return folder_resp.status_code
    def get_folder_list(self):
        folder_list = self.session.get(f'{self.base_url}/resources?path=/')
        if folder_list.status_code == 200:
            lst = folder_list.json()
            print(lst)


if __name__ == '__main__':
    yd = YaDisk()
    yd.get_folder_list()