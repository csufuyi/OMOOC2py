# -*- coding: utf-8 -*-
#!/usr/bin/env python
#   头部声明
'''文件说明
作者信息
版本自述
    ...
'''
# 全局引用
import sys
# 全局变量
PATH = "/path/2/work dir"
# 函式撰写区
def foo():
    print 'hello world'
    print '支持中文的'
    return None

# 自检区
if __name__ == '__main__':
    if 1 != len(sys.argv) :
        print '''Usage:
$ python main.py
        '''
    else:
        foo()





