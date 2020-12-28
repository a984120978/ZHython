str2 = {'！': '!', '￥': '$', '（': '(', '）': ')', '——': '_', '，': ',', '。': '.', '；': ':', '‘': "'", '“': '"',
        '”': '"', '【': '[', '】': ']', '\t': '    '}


def str2_str(s: str) -> str:
    temp = ''
    for i in s:
        if str2.get(i):
            temp += str2.get(i)
        else:
            temp += i
    return temp
