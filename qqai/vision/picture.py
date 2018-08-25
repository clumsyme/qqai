from qqai.classes import *


class SceneR(QQAIPicRecognitionClass):
    """场景识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_scener'

class ObjectR(QQAIPicRecognitionClass):
    """物体识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_objectr'

class Tag(QQAIPicClass):
    """图像标签识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_tag'

class ImgToText(QQAIClass):
    """看图说话"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgtotext'

    def make_params(self, image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_base64(image_param),
                  'session_id': int(time.time()),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param):
        params = self.make_params(image_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class Fuzzy(QQAIPicClass):
    """模糊图片检测"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_fuzzy'

class Food(QQAIPicClass):
    """美食图片识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_food'

class Porn(QQAIPicClass):
    """智能鉴黄"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_porn'

class Terrorism(QQAIPicClass):
    """暴恐图片识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/image/image_terrorism'
