import requests
import json
import os


def upload_img(image_path):
    files_map = [('smfile', image_path)]
    params = {
        'ssl': False,
        'format': 'png'
    }
    multi_files = list(map(lambda x: (x[0], (os.path.split(x[1])[1], open(x[1], 'rb'))), files_map))
    resp = requests.post("https://sm.ms/api/upload", data=params, files=multi_files)
    print(resp.text)
    result = json.loads(resp.text)
    if result['code'] == 'success':
        view_url = result['data']['url']
        del_url = result['data']['delete']
        file_name = result['data']['filename']
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
