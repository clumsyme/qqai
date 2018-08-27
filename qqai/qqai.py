import hashlib
import json
import base64
import time
from urllib import parse
import requests


class BaseRobot:
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
        """获取签名"""
        uri_str = ''
        for key in sorted(params.keys()):
            uri_str += '{}={}&'.format(key,
                                       parse.quote_plus(str(params[key]), safe=''))
        sign_str = uri_str + 'app_key=' + self.app_key

        hash_str = hashlib.md5(sign_str.encode('utf-8'))
        return hash_str.hexdigest().upper()

    def call_api(self, params, api=None):
        if api is None:
            api = self.api

        return requests.post(
            api, data=parse.urlencode(params).encode("utf-8"), headers=self.headers)


class Detectface(BaseRobot):
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_detectface'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'mode': 0,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_image(image_param)}
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param):
        params = self.make_params(image_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result


class TextChat(BaseRobot):
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'

    def __init__(self, app_id, app_key):
        super().__init__(app_id, app_key)
        self.session = str(time.time())

    def make_params(self, question):
        """获取调用接口的参数
        """
        params = {
            'app_id': self.app_id,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'question': question,
            'session': self.session,
        }

        params['sign'] = self.get_sign(params)

        return params

    def ask(self, question):
        """单句聊天"""
        params = self.make_params(question)
        response = self.call_api(params)
        result = json.loads(response.text)
        answer = result['data']['answer']
        return answer

    def chat(self):
        """持续对话"""
        print('< 有啥想跟我说的？')
        while True:
            question = input('> ')
            if question == 'q':
                break
            else:
                answer = self.ask(question)
                print('<', answer)


class ImgToText(BaseRobot):
    """看图说话"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgtotext'

    def make_params(self, image_param):
        """获取调用接口的参数
        """
        params = {'app_id': self.app_id,
                  'session_id': int(time.time()),
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_image(image_param)
        }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param):
        params = self.make_params(image_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class NLPTrans(BaseRobot):
    """文本翻译
    """
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttranslate'

    def __init__(self, app_id, app_key, source='zh', target='en'):
            super().__init__(app_id, app_key)
            self.source = source
            self.target = target

    def make_params(self, text):
        """获取调用接口的参数
        """
        params = {
            'app_id': self.app_id,
            'time_stamp': int(time.time()),
            'nonce_str': int(time.time()),
            'source': self.source,
            'target': self.target,
            'text': text,
        }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param):
        params = self.make_params(image_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result
