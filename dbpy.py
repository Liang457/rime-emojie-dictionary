# 默认为MS双拼
# 韵母替换表
DBPY_YM = [
    ['iu', 'q'],
    ['ia', 'w'],
    ['ua', 'w'],
    ['er', 'r'],
    ['uan', 'r'],
    ['ue', 't'],
    ['uai', 'y'],
    ['v', 'y'],
    ['uo', 'o'],
    ['un', 'p'],
    ['iong', 's'],
    ['ong', 's'],
    ['iang', 'd'],
    ['uang', 'd'],
    ['en', 'f'],
    ['eng', 'g'],
    ['ang', 'h'],
    ['an', 'j'],
    ['ao', 'k'],
    ['ai', 'l'],
    ['ing', ';'],
    ['ei', 'z'],
    ['ie', 'x'],
    ['iao', 'c'],
    ['ui', 'v'],
    ['ve', 'v'],
    ['ou', 'b'],
    ['in', 'n'],
    ['ian', 'm'],
]
# 声母替换表
DBPY_SM = [
    ['sh', 'u'],
    ['ch', 'i'],
    ['zh', 'v']
]
# 零声母替换表
DBPY_OSM = [
    ['a', 'oa'],
    ['e', 'oe'],
    ['o', 'oo'],
    ['ai', 'ol'],
    ['ei', 'oz'],
    ['ou', 'ob'],
    ['an', 'oj'],
    ['en', 'of'],
    ['ang', 'oh'],
    ['eng', 'og'],
    ['ao', 'ok'],
    ['er', 'or']
]


def dbpy_tihr(pinyin: list):
    out_pinyin_list = []
    # 完整的检测
    for py in pinyin:
        for sm in DBPY_SM:
            if sm[0] == py[:1]:
                py = sm[1] + py[1:]
            elif sm[0] == py[:2]:
                py = sm[1] + py[2:]
        for ym in DBPY_YM:
            if ym[0] == py[1:]:
                py = py[0] + ym[1]
        for osm in DBPY_OSM:
            if osm[0] == py:
                py = osm[1]

        out_pinyin_list.append(py)

    return out_pinyin_list


if __name__ == '__main__':
    print(dbpy_tihr(['https://gitee.com/liang2457/rime-emojie-dictionary']))
