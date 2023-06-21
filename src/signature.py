from rsa import RSA
from keccak import Keccak
from typing import List


class Signature:
    """
    Class for signing a message. Message signing is done with RSA and SHA3 algorithm
    """
    __slots__ = "name"
    def __init__(self, name):
        self.name = name


    def sign(self, message: str, private_key: List[int]) -> str:
        """
        Get the signature of a given message.
        """
        keccak = Keccak(self.name, message)
        hash = keccak.hash()
        signature = RSA.encrypt(hash, private_key)
        signed_message = message + "\r\n<ds>\r\n" + signature + "\r\n</ds>"
        return signed_message


    def signOnly(self, message: str, private_key: List[int]) -> str:
        """
        Get the signature of a given message.
        """
        keccak = Keccak(self.name, message)
        hash = keccak.hash()
        signature = RSA.encrypt(hash, private_key)
        return signature


    def verifySignedDocument(self, signed_message: str, public_key: List[int]) -> bool:
        """
        Verify signature of a given signed message.
        """
        signed_message = signed_message.replace('\r\n</ds>', '').replace('\r\n<ds>\r\n', '<ds>')
        signed_message = signed_message.split('<ds>')
        print(signed_message)
        keccak = Keccak(self.name, signed_message[0])
        hash = keccak.hash()

        decrypted = RSA.decrypt(signed_message[1], public_key)

        return hash == decrypted


    def verifySeparatedSignedDocument(self, message: str, signature: str, public_key: List[int]) -> bool:
        """
        Verify signature of a given message and separated signature.
        """
        keccak = Keccak(self.name, message)
        hash = keccak.hash()

        decrypted = RSA.decrypt(signature, public_key)

        return hash == decrypted


def main():
    message = "Test message 1 2 3"
    print("Message:", message)

    keys = RSA.generateKey()
    print("Keys:", keys)

    signa = Signature("SHA3-256")

    signed_message = signa.sign(message, keys[1])
    print("Signed_Message:", signed_message)

    verify = signa.verifySignedDocument(signed_message, keys[0])
    print("Verify:", verify)


if __name__ == "__main__":
    main()