#!/usr/bin/python
#-*-coding:utf-8-*-

import time
import jieba


jieba.enable_parallel()


def main():
    fd = open("../data/tg.txt", "rb")
    fo = open("./tmp.txt", "wb")

    print "Start cut word."
    start = time.time()

    for line in fd.xreadlines():
        fo.write(" ".join(jieba.cut(line)).encode("utf-8"))

    end = time.time()
    time_cost = end - start
    print "Cost time %s." % time_cost
    print "Process file completely."

if __name__ == "__main__":
    main()