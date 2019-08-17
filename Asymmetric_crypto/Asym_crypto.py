import os
import base64
import random
import struct
import hashlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
    )
print(chave_privada)
chave_publica = chave_privada.public_key()
print(chave_publica)

imagem_original = open('imagem.jpg', 'rb').read()

from cryptography.fernet import Fernet
chave_simetrica = Fernet.generate_key()
print(chave_simetrica)
cripto = Fernet(chave_simetrica)
imagem_encriptada = cripto.encrypt(imagem_original)
with open('imagem_encriptada_rsa.jpg','wb') as f:
    f.write(imagem_encriptada)


from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

chave_sim_cript = chave_publica.encrypt(
    chave_simetrica,
    padding.OAEP(
        mgf = padding.MGF1(algorithm=hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
        )
    )
del chave_simetrica
print(chave_sim_cript)

chave_sim_rec = chave_privada.decrypt(
    chave_sim_cript,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
        )
    )

print(chave_sim_rec)
cripto = Fernet(chave_sim_rec)

with open('imagem_encriptada_rsa.jpg', 'r') as img_enc:
    with open('imagem_recuperada_rsa.jpg', 'wb') as img_rec:
        conteudo = cripto.decrypt(str.encode(img_enc.read()))
        img_rec.write(conteudo)