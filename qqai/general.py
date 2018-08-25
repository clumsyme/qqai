import hashlib
import base64
from urllib import parse
import requests


class QQAIClass:
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    imageHeaders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    }

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_image(self, image_param):
        """图片类接口获取 image 参数对象

        :param image_param 图片URL或者图片BufferedReader对象
        """
        if type(image_param) == str:
            image_data = requests.get(
                image_param, headers=self.imageHeaders).content
        elif hasattr(image_param, 'read'):
            image_data = image_param.read()
        else:
            raise TypeError('image must be URL or BufferedReader')

        image = base64.b64encode(image_data).decode("utf-8")
        return image

    def get_sign(self, params):
        """获取签名
        """
        uri_str = ''
        for key in sorted(params.keys()):
            uri_str += '{}={}&'.format(key,
                                       parse.quote(str(params[key]), safe=''))
        sign_str = uri_str + 'app_key=' + self.app_key

        hash_str = hashlib.md5(sign_str.encode('utf-8'))
        return hash_str.hexdigest().upper()

    def call_api(self, params, api=None):
        if api is None:
            api = self.api

        return requests.post(
            api, data=parse.urlencode(params).encode("utf-8"), headers=self.headers)
