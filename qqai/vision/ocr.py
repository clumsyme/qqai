from qqai.classes import *


class IDCardOCR(QQAIClass):
    """身份证OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_idcardocr'

    def make_params(self, image_param, cardtype):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_base64(image_param),
                  'card_type': cardtype,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, cardtype=0):
        params = self.make_params(image_param, cardtype)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class BCOCR(QQAIPicClass):
    """名片OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_bcocr'

class DriverLicenseOCR(QQAIClass):
    """行驶证驾驶证OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_driverlicenseocr'

    def make_params(self, image_param, license_type):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_base64(image_param),
                  'type': license_type,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_param, license_type=1):
        params = self.make_params(image_param, license_type)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class PlateOCR(QQAIPicOrURLClass):
    """车牌OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_plateocr'

class BizLicenseOCR(QQAIPicClass):
    """营业执照OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_bizlicenseocr'

class CreditCardOCR(QQAIPicClass):
    """银行卡OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_creditcardocr'

class GeneralOCR(QQAIPicClass):
    """通用OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr'

class HandwritingOCR(QQAIPicOrURLClass):
    """手写体OCR"""
    api = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_handwritingocr'
