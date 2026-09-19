"""
switch(flag): command line에서 arg 입력 시 특정 동작을 하도록 설정한 특정 문자를 의미
              특정 문자로는 'dash + 단일 문자' 또는 'dash dash + 한 단어'로 사용 (-n, --number, ...)
    -n N: number of times('N' times)
    -h, --help: show help message

argparse: command line arguments(CLAs)에 있는 switch(flag)를 처리하는 library
          argument parser, 즉 CLAs를 읽고 분석하여 처리하는 역할
    >>> https://docs.python.org/3/library/argparse.html
"""


import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")    # instantiate an object of class 'ArgumentParser'
                                                                   # print the string when type '-h(--help)'
parser.add_argument("-n", default=1, help="number of times to meow", type=int)    # add an argument that will be used as switch
                                                                                  # by default N == 1 and 'N' should be integer
                                                                                  # print the string when type '-h(--help)'
args = parser.parse_args()    # an object of 'parser.parse_args'
                              # automatically look at 'sys.argv'
                              # parsed all of the CLAs by 'parser'

for _ in range(args.n):    # 'n' is property in the object, access to it
    print("meow")
