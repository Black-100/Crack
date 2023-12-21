import os, sys
try:
    __import__("crack").main()
except Exception as e:
    exit(str(e))
