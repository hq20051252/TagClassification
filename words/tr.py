#!/usr/bin/python
# -*- coding: utf-8-*-

import sys


def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        # 全角空格直接转换
        if inside_code == 12288:
            inside_code = 32
        # 全角字符（除空格）根据关系转化
        elif (inside_code >= 65281) and (inside_code <= 65374):
            inside_code -= 65248

        rstring += unichr(inside_code)
    return rstring


def strB2Q(ustring):
    """半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        # 半角空格直接转化
        if inside_code == 32:
            inside_code = 12288
        # 半角字符（除空格）根据关系转化
        elif (inside_code >= 32) and (inside_code <= 126):
            inside_code += 65248

        rstring += unichr(inside_code)
    return rstring


def test():

    b = strQ2B("ｍｎ123abc博客园".decode('utf-8'))                           
    print b.encode("utf-8")

    c = strB2Q("ｍｎ123abc博客园".decode('utf-8'))                           
    print c.encode("utf-8")


def usage():
    print "python tr.py <filename>"
    sys.exit(1)


def main():
    if len(sys.argv) == 2:
        f = sys.argv[1]
    else:
        usage()

    with open(f, "rb") as fd:
        for line in fd.xreadlines():
            b = strQ2B(line.decode("utf-8"))
            print b.encode("utf-8")


if __name__ == "__main__":
    # test()
    main()
