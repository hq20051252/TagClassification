#!/usr/bin/python
# -*-coding:utf-8-*-

import sys
import time
import jieba


jieba.enable_parallel()


def usage():
    print "Usage: python file_cut.py <input> <output>"
    sys.exit(1)


def main():
    if len(sys.argv) == 3:
        f = sys.argv[1]
        o = sys.argv[2]

    else:
        usage()

    fd = open(f, "rb")
    fo = open(o, "wb")

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