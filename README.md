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

