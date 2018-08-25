from qqai.general import QQAIClass
import time
import json


class SceneR(QQAIClass):
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

class ObjectR(QQAIClass):
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

class Tag(QQAIClass):
    """图像标签识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_tag'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
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

class ImgToText(QQAIClass):
    """看图说话"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgtotext'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_image(image_param),
                  'session_id': int(time.time())
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param):
        params = self.make_params(image_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class Fuzzy(QQAIClass):
    """模糊图片检测"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_fuzzy'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
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

class Food(QQAIClass):
    """美食图片识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_food'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
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