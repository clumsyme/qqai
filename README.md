# qqai

提供[腾讯AI](https://ai.qq.com/)简单易用的python接口。

## 安装

```bash
pip install qqai
```

## 目前完成的功能

- [ ] 自然语言处理
    - [x] 基础文本分析
        - [x] 分词 (`qqai.nlp.text.WordSeg`)
        - [x] 词性标注 (`qqai.nlp.text.WordPos`)
        - [x] 专有名词识别 (`qqai.nlp.text.WordNer`)
        - [x] 同义词识别 (`qqai.nlp.text.WordSyn`)
    - [x] 语义解析
        - [x] 意图成分识别 (`qqai.nlp.text.WordCom`)
    - [x] 情感分析
        - [x] 情感分析识别 (`qqai.nlp.text.TextPolar`)
    - [x] 智能闲聊
        - [x] 基础闲聊 (`qqai.nlp.text.TextChat`)
    - [ ] 机器翻译
        - [x] 文本翻译
            - [x] 文本翻译（AI Lab） (`qqai.nlp.translate.TextTranslateAILab`)
            - [x] 文本翻译（翻译君） (`qqai.nlp.translate.TextTranslateFanyi`)
        - [x] 图片翻译 (`qqai.nlp.translate.ImageTranslate`)
        - [ ] 语音翻译
        - [x] 语种识别 (`qqai.nlp.translate.TextDetect`)
- [ ] 智能语音
    - [ ] 语音识别
        - [x] 语音识别-echo版 (`qqai.aai.audio.AudioRecognitionEcho`)
        - [ ] 语音识别-流式版（AI Lab）
        - [ ] 语音识别-流式版(WeChat AI)
    - [ ] 长语音识别
    - [ ] 关键词检索
    - [x] 语音合成
        - [x] 语音合成（AI Lab） (`qqai.aai.tts.TTSAILab`)
        - [x] 语音合成（优图） (`qqai.aai.tts.TTSYouTu`)
- [x] 计算机视觉
    - [x] 智能鉴黄 (`qqai.vision.picture.Porn`)
    - [x] 暴恐识别 (`qqai.vision.picture.Terrorism`)
    - [x] 优图OCR
        - [x] 身份证OCR (`qqai.vision.ocr.IDCardOCR`)
        - [x] 名片OCR (`qqai.vision.ocr.BCOCR`)
        - [x] 行驶证驾驶证OCR (`qqai.vision.ocr.DriverLicenseOCR`)
        - [x] 车牌OCR (`qqai.vision.ocr.PlateOCR`)
        - [x] 营业执照OCR (`qqai.vision.ocr.BizLicenseOCR`)
        - [x] 银行卡OCR (`qqai.vision.ocr.CreditCardOCR`)
        - [x] 通用OCR (`qqai.vision.ocr.GeneralOCR`)
        - [x] 手写体OCR (`qqai.vision.ocr.HandwritingOCR`)
    - [x] 人脸识别
        - [x] 人脸检测与分析 (`qqai.vision.face.DetectFace`)
        - [x] 多人脸检测 (`qqai.vision.face.DetectMultiFace`)
        - [x] 人脸对比 (`qqai.vision.face.FaceCompare`)
        - [x] 跨年龄人脸识别 (`qqai.vision.face.DetectCrossAgeFace`)
        - [x] 五官定位 (`qqai.vision.face.FaceShape`)
        - [x] 人脸识别 (`qqai.vision.face.FaceIdentify`)
        - [x] 人脸验证 (`qqai.vision.face.FaceVerify`)
        - [x] 个体管理
            - [x] 个体创建 (`qqai.vision.face.NewPerson`)
            - [x] 删除个体 (`qqai.vision.face.DelPerson`)
            - [x] 增加人脸 (`qqai.vision.face.AddFace`)
            - [x] 删除人脸 (`qqai.vision.face.DelFace`)
            - [x] 设置信息 (`qqai.vision.face.SetInfo`)
            - [x] 获取信息 (`qqai.vision.face.GetInfo`)
        - [x] 信息查询
            - [x] 获取组列表 (`qqai.vision.face.GetGroupIds`)
            - [x] 获取个体列表 (`qqai.vision.face.GetPersonIds`)
            - [x] 获取人脸列表 (`qqai.vision.face.GetFaceIds`)
            - [x] 获取人脸信息 (`qqai.vision.face.GetFaceInfo`)
    - [x] 图片识别
        - [x] 物体场景识别
            - [x] 场景识别 (`qqai.vision.picture.SceneR`)
            - [x] 物体识别 (`qqai.vision.picture.ObjectR`)
        - [x] 图片标签识别 (`qqai.vision.picture.Tag`)
        - [x] 看图说话 (`qqai.vision.picture.ImgToText`)
        - [x] 模糊图片检测 (`qqai.vision.picture.Fuzzy`)
        - [x] 美食图片识别 (`qqai.vision.picture.Food`)
    - [x] 图片特效
        - [x] 人脸美妆 (`qqai.vision.ptu.FaceCosmetic`)
        - [x] 人脸变妆 (`qqai.vision.ptu.FaceDecoration`)
        - [x] 滤镜
            - [x] 滤镜（天天P图） (`qqai.vision.ptu.ImgFilterPitu`)
            - [x] 滤镜（AI Lab） (`qqai.vision.ptu.ImgFilterAILab`)
        - [x] 人脸融合 (`qqai.vision.ptu.FaceMerge`)
        - [x] 大头贴 (`qqai.vision.ptu.FaceSticker`)
        - [x] 颜龄检测 (`qqai.vision.ptu.FaceAge`)

## 调用方式

可以直接导入包，再使用其中的类；也可以导入子包或类。

调用类的时候定义好AppID和AppKey。

各个类都有一个`run()`方法以执行操作。该方法参数有所不同，请查阅开发平台文档和代码以输入。

以下为示例：

```python
import qqai
qqai.vision.picture.ImgToText('your_app_id', 'your_app_key').run('https://yyb.gtimg.com/aiplat/ai/assets/ai-demo/express-6.jpg')
# {'ret': 0, 'msg': 'ok', 'data': {'text': '一位男士在海边骑自行车的照片'}}

from qqai.vision.picture import ImgToText
it = ImgToText('your_app_id', 'your_app_key')
it.run('https://yyb.gtimg.com/aiplat/ai/assets/ai-demo/express-6.jpg')
# {'ret': 0, 'msg': 'ok', 'data': {'text': '一位男士在海边骑自行车的照片'}}
```


## 用法（原文档）

当前包含以下接口：

- [聊天机器人](#聊天机器人)
- [文本翻译](#文本翻译)
- [图片转文字](#图片转文字)
- [人脸检测](#人脸检测)

### 聊天机器人

```py
from qqai import TextChat

siri = TextChat(your_app_id, your_app_key)

# 单句对话
answer = siri.ask('你是谁')
print(answer)
# >>> 我是你的小助手啊

# 连续聊天
siri.chat()
# < 有啥想跟我说的？
# > 你是谁啊？
# < 我是你的小助手啊
# > 你能干嘛呀
# < 呵呵，我能干的事情多的数不清。
```

### 文本翻译

可用语言见[官方文档](https://ai.qq.com/doc/nlptrans.shtml#5-%E6%94%AF%E6%8C%81%E8%AF%AD%E8%A8%80%E5%AE%9A%E4%B9%89)

```py
from qqai import NLPTrans

robot = NLPTrans(you_app_id, you_app_key)

result = robot.run('愿原力与你同在')
print(result)
# {'ret': 0, 'msg': 'ok', 'data': {'source_text': '愿原力与你同在', 'target_text': 'May the Force be with you'}}

# 默认为中英翻译，若需要其他语种翻译，请按以下格式实例化：
# source为源语言，target为目标语言，
robot = NLPTrans(you_app_id, you_app_key, source='en', target='es')

result = robot.run('May the force be with you.')
print(result)
# {'ret': 0, 'msg': 'ok', 'data': {'source_text': 'May the force be with you.', 'target_text': 'Que la fuerza esté contigo.'}}
```

### 图片转文字

```py
from qqai import ImgToText

robot = ImgToText(your_app_id, your_app_key)

# 识别图片URL
result = robot.run('https://yyb.gtimg.com/aiplat/ai/assets/ai-demo/express-6.jpg')
print(result)
# {'ret': 0, 'msg': 'ok', 'data': {'text': '一位男士在海边骑自行车的照片'}}

# 识别打开的本地图片
with open('/my/img.jpeg', 'rb') as image_file:
    result = robot.run(image_file)
    print(result)
# {'ret': 0, 'msg': 'ok', 'data': {'text': '一艘飞船'}}
```

### 人脸检测

```py
from qqai import Detectface

robot = Detectface(your_app_id, your_app_key)

# 调用方法与图片转文字相同
```
