from qqai.classes import *

class WordSeg(QQAITextGBKClass):
    """分词"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordseg'

class WordPos(QQAITextGBKClass):
    """词性标注"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos'

class WordNer(QQAITextGBKClass):
    """专有名词识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordner'

class WordSyn(QQAITextGBKClass):
    """同义词识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordsyn'

class WordCom(QQAITextUTF8Class):
    """意图成分识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordcom'

class TextPolar(QQAITextUTF8Class):
    """情感分析识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar'

class TextChat(QQAIClass):
    """基础闲聊"""
    api = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'

    def make_params(self, session, question):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'session': session,
                  'question': question,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, session, question):
        params = self.make_params(session, question)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

