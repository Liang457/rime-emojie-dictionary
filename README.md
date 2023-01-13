# RIME EMOJIE 词典

爬取 [emojiall]([www.emojiall.com](https://www.emojiall.com/zh-hans)) 获取的 Rime Emojie 词库

## 使用

由于 Gitee 判断词库文件含有违规信息，请转移到[百度网盘](https://pan.baidu.com/s/1Sip2bFi-3bmc5y9Bo7M2xQ?pwd=8shk)下载。或者参见[重新生成](#重新生成)来生成一个。

下载 `对应的词库文件` 后重命名为 `emojie.dict.yaml` 放入到用户文件夹内。然后弄好你的词库配置就可以了

## 提醒

**不确定拼音/双拼的拼音是正确的，也不确定emojie是否能够正确地打出来、显示出来。**

## 重新生成

安装 [`pypinyin`](https://github.com/mozillazg/python-pinyin) 库后运行 `main.py` 就可以了（当然，要确保有网络链接，毕竟是爬虫）

可以在 `main.py` 内设置是否使用双拼和默认词频（默认词频我咋感觉没啥用）

### 使用你的双拼方案

在 `dbpy.py` 内把你的双拼映射写好就可以了。你可以看着默认的微软双拼改。
