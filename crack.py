import os, sys
try:
    __import__("crak").menu()
except Exception as e:
    exit(str(e))
