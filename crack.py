import os, sys
try:
    __import__("Dn").main()
except Exception as e:
    exit(str(e))
