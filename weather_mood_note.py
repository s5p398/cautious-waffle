import random
from datetime import datetime

# 随机天气心情便签生成器

def generate_weather_mood_note():
    # 定义天气列表
    weathers = ["晴天", "多云", "雨天", "阴天", "下雪"]
    
    # 随机选择天气
    weather = random.choice(weathers)
    
    # 天气对应的心情文案字典
    mood_messages = {
        "晴天": "阳光明媚，心情也跟着亮起来了！",
        "多云": "天空有点阴，但还是要保持好心情哦~",
        "雨天": "听雨发呆，悠闲又治愈",
        "阴天": "虽然阴天，但我们可以自己制造阳光！",
        "下雪": "银装素裹，浪漫又宁静的一天"
    }
    
    # 根据天气获取对应心情
    mood = mood_messages[weather]
    
    # 获取当前时间并格式化
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 组合便签内容
    note_content = f"""===== 今日天气心情便签 =====
生成时间：{current_time}
天气：{weather}
心情：{mood}"""
    
    # 输出到控制台
    print(note_content)
    print()
    
    # 保存到本地文件
    filename = "天气便签.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(note_content)
    
    print(f"便签已保存到 {filename}")

if __name__ == "__main__":
    generate_weather_mood_note()
