from qqai.classes import *

class DetectFace(QQAIFaceClass):
    """人脸检测与分析"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_detectface'

class DetectMultiFace(QQAIPicClass):
    """多人脸检测"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_detectmultiface'

class FaceCompare(QQAIClass):
    """人脸对比"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_facecompare'

    def make_params(self, image_a_param, image_b_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image_a': self.get_base64(image_a_param),
                  'image_b': self.get_base64(image_b_param),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image_a_param, image_b_param):
        params = self.make_params(image_a_param, image_b_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class DetectCrossAgeFace(QQAIClass):
    """跨年龄人脸识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_detectcrossageface'

    def make_params(self, source_image_param, target_image_param):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'source_image': self.get_base64(source_image_param),
                  'target_image': self.get_base64(target_image_param),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, source_image_param, target_image_param):
        params = self.make_params(source_image_param, target_image_param)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class FaceShape(QQAIFaceClass):
    """五官定位"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_faceshape'

class FaceIdentify(QQAIClass):
    """人脸识别"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_faceidentify'

    def make_params(self, image, group_id, topn):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_base64(image),
                  'group_id': group_id,
                  'topn': topn,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image, group_id, topn=9):
        params = self.make_params(image, group_id, topn)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class FaceVerify(QQAIClass):
    """人脸验证"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_faceverify'

    def make_params(self, image, person_id):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'image': self.get_base64(image),
                  'person_id': person_id,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, image, person_id):
        params = self.make_params(image, person_id)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class NewPerson(QQAIClass):
    """个体创建"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_newperson'

    def make_params(self, group_ids, person_id, image, person_name, tag=None):
        """获取调用接口的参数"""
        if type(group_ids) == str:
            group_ids_param = group_ids
        else:
            group_ids_param = '|'.join(group_ids)
            # 这里是猜测。文档中疑似转义发生错误，留下反斜杠，之后的字符不见了
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'group_ids': group_ids_param,
                  'person_id': person_id,
                  'image': self.get_base64(image),
                  'person_name': person_name,
                  }
        if tag is not None:
            params['tag'] = tag
        params['sign'] = self.get_sign(params)
        return params

    def run(self, group_ids, person_id, image, person_name, tag=None):
        params = self.make_params(group_ids, person_id, image, person_name, tag)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class DelPerson(QQAIFacePersonClass):
    """删除个体"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_delperson'

class AddFace(QQAIClass):
    """个体创建"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_addface'

    def make_params(self, person_id, images, tag):
        """获取调用接口的参数"""
        if type(images) == str or hasattr(images, 'read'):
            images_param = self.get_base64(images)
        else:
            if len(images) > 5:
                raise ValueError('No more than 5 images input in one request')
            else:
                images_param = '|'.join(map(self.get_base64, images))
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'person_id': person_id,
                  'images': images_param,
                  'tag': tag,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, person_id, images, tag):
        params = self.make_params(person_id, images, tag)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class DelFace(QQAIClass):
    """删除人脸"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_delface'

    def make_params(self, person_id, face_ids):
        """获取调用接口的参数"""
        if type(face_ids) == str:
            face_ids_param = face_ids
        else:
            face_ids_param = '|'.join(face_ids)
            # 这里是猜测。文档中疑似转义发生错误，留下反斜杠，之后的字符不见了
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'person_id': person_id,
                  'face_ids': face_ids_param,
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, person_id, face_ids):
        params = self.make_params(person_id, face_ids)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class SetInfo(QQAIClass):
    """设置信息"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_setinfo'

    def make_params(self, person_id, person_name=None, tag=None):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'person_id': person_id,
                  }
        if person_name is not None:
            params['person_name'] = person_name
        if tag is not None:
            params['tag'] = tag
        params['sign'] = self.get_sign(params)
        return params

    def run(self, person_id, person_name=None, tag=None):
        params = self.make_params(person_id, person_name, tag)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class GetInfo(QQAIFacePersonClass):
    """获取信息"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_getinfo'

class GetGroupIds(QQAIClass):
    """获取组列表"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_getgroupids'

    def make_params(self):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self):
        params = self.make_params()
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class GetPersonIds(QQAIClass):
    """获取个体列表"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_getpersonids'

    def make_params(self, group_id):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'group_id': group_id
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, group_id):
        params = self.make_params(group_id)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class GetFaceIds(QQAIClass):
    """获取人脸列表"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_getfaceids'

    def make_params(self, person_id):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'person_id': person_id
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, person_id):
        params = self.make_params(person_id)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result

class GetFaceInfo(QQAIClass):
    """获取人脸信息"""
    api = 'https://api.ai.qq.com/fcgi-bin/face/face_getfaceinfo'

    def make_params(self, face_id):
        """获取调用接口的参数"""
        params = {'app_id': self.app_id,
                  'time_stamp': int(time.time()),
                  'nonce_str': int(time.time()),
                  'person_id': face_id
                  }
        params['sign'] = self.get_sign(params)
        return params

    def run(self, face_id):
        params = self.make_params(face_id)
        response = self.call_api(params)
        result = json.loads(response.text)
        return result