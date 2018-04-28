from rsa_decryption_125 import decryptor

encrypted = '082976371981814231505650853440353277596004250518494162922046540928633792779152973836494176019498125267683832244888922046522776395123915899132032620457568301878543623328746341710542'

print('Encrypted message: {}'.format(encrypted))
print('Public key: ({}, {})'.format(999797, 123457))
print('--- (decrypting...)')

decrypted = decryptor.decrypt(encrypted, 999797, 123457)
print('Decrypted message: "{}"'.format(decryptor.decode_message(decrypted)))
