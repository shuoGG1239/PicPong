import json
import os
import urllib

import requests

conf_json = json.load(open("config.json"))

def upload_img(image_path):
    if conf_json is None:
        raise Exception("conf_json is None")
    files_map = [('smfile', image_path)]
    file_name = os.path.split(image_path)[1]
    params = {
        'format': 'json'
    }
    multi_files = list(map(lambda x: (x[0], (urllib.parse.quote(os.path.split(x[1])[1]), open(x[1], 'rb'))), files_map))
    header = {
        "Authorization": conf_json["SecretToken"]
    }
    resp = requests.post("https://sm.ms/api/v2/upload", data=params, files=multi_files, headers=header)
    print(resp.text)
    result = json.loads(resp.text)
    if result['code'] == 'success':
        view_url = result['data']['url']
        del_url = result['data']['delete']
        resp_dict = {'url': view_url, 'delete': del_url, 'filename': file_name, 'success': True}
        print(view_url)
        print(del_url)
    elif result['code'] == 'error':
        resp_dict = {'success': False, 'msg': result['msg']}
        print('upload failed! Reason:' + result['msg'])
    else:
        resp_dict = {'success': False, 'msg': 'unknown error'}
        print("upload failed! Unknown reason...")
    return resp_dict


def delete_img(del_url):
    requests.get(del_url)
