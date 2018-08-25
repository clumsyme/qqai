# qqai

提供[腾讯AI](https://ai.qq.com/)简单易用的python接口。

## 安装

```bash
pip install qqai
```

## 用法

当前包含以下接口：

- [聊天机器人](#聊天机器人)
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



## 完成功能

- [ ] 自然语言处理
    - [ ] 基础文本分析
    - [ ] 语义解析
    - [ ] 情感分析
    - [ ] 智能闲聊
    - [ ] 机器翻译
        - [ ] 文本翻译
        - [ ] 图片翻译
        - [ ] 语音翻译
        - [ ] 语种识别
- [ ] 智能语音
    - [ ] 语音识别
    - [ ] 长语音识别
    - [ ] 关键词检索
    - [ ] 语音合成
- [x] 计算机视觉
    - [x] 智能鉴黄
    - [x] 暴恐识别
    - [x] 优图OCR
        - [x] 身份证OCR
        - [x] 名片OCR
        - [x] 行驶证驾驶证OCR
        - [x] 车牌OCR
        - [x] 营业执照OCR
        - [x] 银行卡OCR
        - [x] 通用OCR
        - [x] 手写体OCR
    - [x] 人脸识别
        - [x] 人脸检测与分析
        - [x] 多人脸检测
        - [x] 人脸对比
        - [x] 跨年龄人脸识别
        - [x] 五官定位
        - [x] 人脸识别
        - [x] 人脸验证
        - [x] 个体管理
            - [x] 个体创建
            - [x] 删除个体
            - [x] 增加人脸
            - [x] 删除人脸
            - [x] 设置信息
            - [x] 获取信息
        - [x] 信息查询
            - [x] 获取组列表
            - [x] 获取个体列表
            - [x] 获取人脸列表
            - [x] 获取人脸信息
    - [x] 图片识别
        - [x] 物体场景识别
            - [x] 场景识别
            - [x] 物体识别
        - [x] 图片标签识别
        - [x] 看图说话
        - [x] 模糊图片检测
        - [x] 美食图片识别
    - [x] 图片特效
        - [x] 人脸美妆
        - [x] 人脸变妆
        - [x] 滤镜
            - [x] 滤镜（天天P图）
            - [x] 滤镜（AI Lab）
        - [x] 人脸融合
        - [x] 大头贴
        - [x] 颜龄检测

## 调用方式

```python
import qqai
qqai.nlp.WordSeg('xxxxxx', 'xxxxxx').run('XXXXXXXX')

qqai.vision.ImgToText('xxxxx', 'xxxxxx').run('https://yyb.gtimg.com/aiplat/ai/assets/ai-demo/express-6.jpg')

# {'ret': 0, 'msg': 'ok', 'data': {'text': '一位男士在海边骑自行车的照片'}}

import qqai
ws = qqai.nlp.WordSeg('xxxxx', 'xxxxxx')
ws.run('XXXX')

```