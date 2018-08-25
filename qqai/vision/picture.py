from qqai.general import QQAIClass
import time
import json


class ImgToText(QQAIClass):
    """看图说话"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgtotext'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'session_id': int(time.time()),
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

class Scener(QQAIClass):
    """场景识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_scener'
    def make_params(self, image_param, api_format, topk):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'format': api_format,
                  'topk': topk,
                  'image': self.get_image(image_param)}
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, api_format=1, topk=5):
        params = self.make_params(image_param, api_format, topk)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class Objectr(QQAIClass):
    """物体识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_objectr'
    def make_params(self, image_param, api_format, topk):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'format': api_format,
                  'topk': topk,
                  'image': self.get_image(image_param)}
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, api_format=1, topk=5):
        params = self.make_params(image_param, api_format, topk)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result