import base64
import nacl.utils

def random() -> bytes:
  return base64.b64encode(nacl.utils.random())

print(random())