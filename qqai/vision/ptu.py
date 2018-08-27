from qqai.classes import *


class FaceCosmetic(QQAIClass):
    """人脸美妆"""
    api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facecosmetic'

    def make_params(self, image_param, cosmetic):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'cosmetic': cosmetic,
                  'image': self.get_base64(image_param),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, cosmetic):
        params = self.make_params(image_param, cosmetic)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class FaceDecoration(QQAIClass):
    """人脸变妆"""
    api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facedecoration'

    def make_params(self, image_param, decoration):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'decoration': decoration,
                  'image': self.get_base64(image_param),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, decoration):
        params = self.make_params(image_param, decoration)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class ImgFilterPitu(QQAIClass):
    """图片滤镜（天天P图）"""
    api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_imgfilter'

    def make_params(self, image_param, pic_filter):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'filter': pic_filter,
                  'image': self.get_base64(image_param),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, pic_filter):
        params = self.make_params(image_param, pic_filter)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class ImgFilterAILab(QQAIClass):
    """图片滤镜（AI Lab）"""
    api = 'https://api.ai.qq.com/fcgi-bin/vision/vision_imgfilter'

    def make_params(self, image_param, pic_filter):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'filter': pic_filter,
                  'image': self.get_base64(image_param),
                  'session_id': int(time.time()),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, pic_filter):
        params = self.make_params(image_param, pic_filter)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class FaceMerge(QQAIClass):
    """人脸融合"""
    api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facemerge'

    def make_params(self, image_param, model):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'model': model,
                  'image': self.get_base64(image_param),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, model):
        params = self.make_params(image_param, model)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class FaceSticker(QQAIClass):
    """大头贴"""
    api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facesticker'

    def make_params(self, image_param, sticker):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'sticker': sticker,
                  'image': self.get_base64(image_param),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, sticker):
        params = self.make_params(image_param, sticker)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class FaceAge(QQAIPicClass):
    """颜龄检测"""
    api = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_faceage'
