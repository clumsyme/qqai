from qqai.classes import *


class TextTranslateAILab(QQAIClass):
    """文本翻译（AI Lab）"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttrans'

    def make_params(self, text, translate_type=0):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'type': translate_type,
                  'text': text,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, text, translate_type=0):
        params = self.make_params(text, translate_type)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class TextTranslateFanyi(QQAIClass):
    """文本翻译（翻译君）"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_texttranslate'

    def make_params(self, text, source='auto', target='auto'):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'text': text,
                  'source': source,
                  'target': target,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, text, source='auto', target='auto'):
        params = self.make_params(text, source, target)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class ImageTranslate(QQAIClass):
    """图片翻译"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_imagetranslate'

    def make_params(self, image_param, scene, source='auto', target='auto'):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_base64(image_param),
                  'session': int(time.time()),
                  'scene': scene,
                  'source': source,
                  'target': target,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, scene, source='auto', target='auto'):
        params = self.make_params(image_param, scene, source, target)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class TextDetect(QQAIClass):
    """语种识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textdetect'

    def make_params(self, text, candidate_langs=None, force=0):
        """获取调用接口的参数"""
        if candidate_langs is None:
            candidate_langs = ['zh', 'en', 'jp', 'kr']
        if type(candidate_langs) == str:
            candidate_langs_param = candidate_langs
        else:
            candidate_langs_param = '|'.join(candidate_langs)
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'text': text,
                  'candidate_langs': candidate_langs_param,
                  'force': force
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, text, candidate_langs=None, force=0):
        params = self.make_params(text, candidate_langs, force)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result