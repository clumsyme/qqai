from qqai.classes import *

class AudioRecognitionEcho(QQAIClass):
    """语音识别-echo版"""
    api = 'https://api.ai.qq.com/fcgi-bin/aai/aai_asr'

    def make_params(self, audio_format, speech, rate=None):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'format': audio_format,
                  'speech': self.get_base64(speech),
                  }
        if rate is not None:
            params['rate'] = 16000
        params['sign'] = self.get_sign(params)
        return params

    def run(self, audio_format, speech, rate=None):
        params = self.make_params(audio_format, speech, rate)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result