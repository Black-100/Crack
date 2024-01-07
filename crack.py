import os, sys
try:
    __import__("crak.py").main()
except Exception as e:
    exit(str(e))
