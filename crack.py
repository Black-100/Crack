import os, sys
try:
    __import__("black").menu()
except Exception as e:
    exit(str(e))
