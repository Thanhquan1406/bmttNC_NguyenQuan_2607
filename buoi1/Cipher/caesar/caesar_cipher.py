from Cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text_upper = text.upper()
        encrypted_text = []
        for letter in text_upper:
            output_letter = self.alphabet.index(letter)
            output_letter = (output_letter + key) % alphabet_len
            output_letter = self.alphabet[output_letter]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text_upper = text.upper()
        decrypted_text = []
        for letter in text_upper:
            letter_index = self.alphabet.index(letter)
            output_letter = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[output_letter]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)