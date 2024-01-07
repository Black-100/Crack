import os, sys
try:
    __import__("menu").main()
except Exception as e:
    exit(str(e))
