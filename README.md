# qqai

提供[腾讯AI](https://ai.qq.com/)简单易用的python接口。

## 安装

```bash
pip install qqai
```

## 用法

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

# 默认为中英翻译，若需要其他语种翻译，请按一下格式实例化：
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

