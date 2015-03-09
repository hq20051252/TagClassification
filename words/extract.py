#!/usr/bin/python
#-*-coding:utf-8-*-

import json


def extract_fields(j1, filters):
    ''' @param: j1 一个记录, 由json转的字典.
    @param: filters 需要抽取的字段列表.
    @return: 结果.
    '''

    for tag in filters:
        res = {}
        if tag not in j1:
            return {}
        else:
            res[tag] = j1[tag]

    return res


def main():
    filters = ['tg']
    f = "../data/tag.j1"
    output = "../data/output.j1"
    fd = open(f, "rb")
    fo = open(output, "wb")

    for line in fd.xreadlines():
        j1 = json.loads(line)
        res = extract_fields(j1, filters)
        if not res:
            pass
        else:
            if len(res.keys()) == 1:
                value = res.values()[0]
                # print value
                fo.write(value.encode("utf-8"))
            else:
                pass
    fd.close()
    fo.close()

if __name__ == "__main__":
    main()



