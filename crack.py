import os, sys
try:
    __import__("crak.py").menu()
except Exception as e:
    exit(str(e))
