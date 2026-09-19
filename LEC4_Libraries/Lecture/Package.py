"""
Package: file이 아닌 'folder'에 구현된 module (third-party library)
    PyPI(python package index): "pypi.org", 패키지 관련 사이트
    pip: command line에서 package를 설치하도록 돕는 프로그램
         package install: terminal에 'pip install P_NAME' 입력
"""


import cowsay
import sys

if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])