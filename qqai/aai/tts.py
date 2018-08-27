from qqai.classes import *

class TTSAILab(QQAIClass):
    """语音合成（AI Lab）"""
    api = 'https://api.ai.qq.com/fcgi-bin/aai/aai_tts'

    def make_params(self, text, speaker, audio_format, volume=0, speed=100,
                    aht=0, apc=58):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'text': text,
                  'speaker': speaker,
                  'format': audio_format,
                  'volume': volume,
                  'speed': speed,
                  'aht': aht,
                  'apc': apc,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, text, speaker, audio_format, volume=0, speed=100, aht=0,
            apc=58):
        params = self.make_params(text, speaker, audio_format, volume, speed,
                                  aht, apc)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class TTSYouTu(QQAIClass):
    """语音合成（优图）"""
    api = 'https://api.ai.qq.com/fcgi-bin/aai/aai_tta'

    def make_params(self, text, model_type=0, speed=0):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'text': text,
                  'model_type': model_type,
                  'speed': speed,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, text, model_type=0, speed=0):
        params = self.make_params(text, model_type, speed)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result