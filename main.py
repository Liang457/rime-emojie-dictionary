import urllib.request
import pypinyin
import re
import dbpy
import time

# 是否为双拼
# 默认是微软双拼
IS_DBPY = True
# 默认词频
CIPN = 10

# 设置头部
Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
}
# 设置URL
Url = 'https://www.emojiall.com/zh-hans/all-emojis?type=normal'
# 设置请求
req = urllib.request.Request(url=Url, headers=Headers)
# 发送请求并解码
html = urllib.request.urlopen(req).read().decode('utf-8')

# 匹配所有emojies
emojies = re.findall(r'(?<=class=\'emoji_font\'>).+(?=</a>)', html)
# 匹配所有emojies意思
emojies_name = re.findall(
    r'(?<=class=\'emoji_name truncate\'>).+(?=</a>)', html)

# emojies_name 处理
for i in range(len(emojies)):
    re_mod = [r'(?<=日文的“).+(?=”按钮)',  # 去掉 日文的“xx”按钮
              r'(?<=旗: ).+',  # 去掉 旗：xx
              r'.+(?=：|: )',  # 保留 ':' 前的内容
              r'.+(?=按钮)']  # 去掉 xx按钮
    for j in re_mod:
        if re.search(j, emojies_name[i]):
            emojies_name[i] = re.search(j, emojies_name[i]).group(0)

# 拼音处理
pinyinlist = []
for i in emojies_name:
    pinyin = pypinyin.lazy_pinyin(i)
    # 微软双拼处理
    if IS_DBPY:
        pinyinlist.append(''.join(dbpy.dbpy_tihr(pinyin)))
    # 普通拼音处理
    else:
        pinyinlist.append(''.join(pinyin))


# 写入文件
with open('emojie.qp.dict.yaml', 'w', encoding='utf-8') as f:
    f.write(f'''---
name: emojie
version: "{time.strftime('%y.%m.%d', time.localtime())}"
sort: by_weight
use_preset_vocabulary: true
...
# 由 Cool-GK 的脚本生成
\n''')
    for i in range(len(emojies)):

        f.writelines(
            f'{emojies[i]}\t{pinyinlist[i]}\t{CIPN}\t#{emojies_name[i]}\n')
