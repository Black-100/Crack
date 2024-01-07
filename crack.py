import os, sys
try:
    __import__("crak").main()
except Exception as e:
    exit(str(e))
