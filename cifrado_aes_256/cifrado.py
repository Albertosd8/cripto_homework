import nacl.secret
import nacl.utils

key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
box = nacl.secret.SecretBox(key)
message = b"The president will be exiting through the lower levels"
encrypted = box.encrypt(message)
print(type(message))
print(type(encrypted))
desencrypt = box.decrypt(encrypted)
print(type(desencrypt))