# -------- WELCOME! -------
# -Please read the comments above the provided interfaces and classes carefully.
#
# -For checking out sample code explaining use of the IFile and ICharCipher interfaces,
# see the 'SampleCode' class.
#
# -You need to write your main solution code inside the provided class 'EncryptedFile'.
# You may write more classes and functions, and include additional headers as needed.
#
# -You don't need to write any code inside main(). The reading of console input, printing of output,
# etc. is already written for you and the program also calls your 'EncryptedFile' class.
# However, you may write any additional code in main() to test out your solution. Please remove
# any test code you write inside main() before submitting.
#
# -The interfaces and classes of interest to you in this file are 'IFile', 'EncryptedFile',
# 'ICharCipher', 'CharCipherFactory' and 'SampleCode'. You may ignore code inside
# 'EncryptedFileTest', 'MemoryFile', 'CaesarCipher' classes.

from abc import ABC, abstractmethod


#
# IFile represents a file and various operations on the file. For simplicity,
# file can store only a-z (lower-case) chars only.
#
class IFile(ABC):

    #
    # Reads no_of_bytes_to_read bytes in bytes_read from offset.
    #
    # It reads only available bytes if available bytes are lesser than
    # requested bytes.
    #
    # @param offset 0 indexed offset from where to start reading bytes
    # @param no_of_bytes_to_read total number of bytes to read
    # @param bytes_read filled with bytes read from the file
    # @return no of bytes actually read, can be less than no_of_bytes_to_read if
    #         enough bytes are not available, 0 if end of file is reached
    @abstractmethod
    def read(self, offset: int, no_of_bytes_to_read: int, bytes_read: bytearray) -> int:
        pass

    #
    # Writes no_of_bytes_to_write bytes from bytes_to_write at offset.
    #
    # It increases the size of the file if offset is beyond end of the file.
    #
    # @param offset 0 indexed offset at where to start writing bytes.
    # @param no_of_bytes_to_write total number of bytes to write
    # @param bytes_to_write bytes to write
    # @return no of bytes actually written, can be less than no_of_bytes_to_write in some scenarios
    #
    @abstractmethod
    def write(self, offset: int, no_of_bytes_to_write: int, bytes_to_write: bytearray) -> int:
        pass

    #
    # Changes the size of the file.
    #
    # If new file size is higher than current file size, fill extra content with 'a'.
    # If new file size is lower than current file size, extra content is stripped.
    #
    # @param new_size new size of the file
    #
    @abstractmethod
    def set_size(self, new_size: int):
        pass

    #
    # Returns the size of the file.
    #
    # @return the size of the file
    #
    @abstractmethod
    def get_size(self) -> int:
        pass

    #
    # Returns the content of the file.
    #
    # @return reference of the underlying char array storing file content
    #
    @abstractmethod
    def get_contents(self) -> bytearray:
        pass


#
#
# MemoryFile represents in-memory buffer as IFile.
#
#
class MemoryFile(IFile):
    def __init__(self, initial_content: bytearray):
        self.content = initial_content
        self.size = len(initial_content)

    def read(self, offset: int, no_of_bytes_to_read: int, bytes_read: bytearray) -> int:
        if offset >= self.size:
            return 0

        no_of_bytes_to_read = min((self.size - offset), no_of_bytes_to_read)
        bytes_read[0:no_of_bytes_to_read] = self.content[offset:offset + no_of_bytes_to_read]
        return no_of_bytes_to_read

    def write(self, offset: int, no_of_bytes_to_write: int, bytes_to_write: bytearray) -> int:
        if (offset + no_of_bytes_to_write) > self.size:
            self.set_size(offset + no_of_bytes_to_write)
        self.content[offset:(offset + no_of_bytes_to_write)] = bytes_to_write[0:no_of_bytes_to_write]
        return no_of_bytes_to_write

    def set_size(self, new_size: int):
        buffer = bytearray(b'a') * new_size
        size_of_data_to_be_copied = min(self.size, new_size)
        buffer[0:size_of_data_to_be_copied] = self.content[0:size_of_data_to_be_copied]
        self.content = buffer
        self.size = new_size

    def get_size(self) -> int:
        return self.size

    def get_contents(self) -> bytearray:
        return self.content


#
# ICharCipher represents an 8-chars block cipher which encrypts and decrypts
# characters only. For simplicity, it only handles a-z (lower-case) letters.
#
# It is a block cipher which means data can be encrypted and decrypted in
# chunk of block length only. If the length of the data to be encrypted is not
# aligned to block length, last block is padded with dummy chars. An extra last
# block is added to encrypted data containing information regarding padding,
# like padding count, etc. This extra block is always added, even if padding is
# not required.
# For simplicity, assume that block length is 8-chars only.
#
# Examples:
# Assume 'm' means plain char, 'c' means ciphered (encrypted) char, 'd' means dummy padded data 
# and 'p' means padding info char.
#
# Example 1: 16-char data.
# Plain:		| mmmmmmmm | mmmmmmmm |
# Encrypted:	| cccccccc | cccccccc | pppppppp |
#
# Example 1: 12-char data.
# Plain:		| mmmmmmmm | mmmm |
# Plain+Padded: | mmmmmmmm | mmmmdddd |
# Encrypted:	| cccccccc | cccccccc | pppppppp |
#
#

class ICharCipher(ABC):
    #
    # Returns the block length.
    #
    # @return  block length
    #
    @abstractmethod
    def get_block_length(self) -> int:
        pass

    #
    # Encrypts a single block from plain_bytes starting from
    # plain_bytes_offset and copies it into enc_bytes at enc_bytes_offset.
    #
    # This method encrypts single block only. In case it is a last
    # block, no_of_bytes_to_encrypt should be set to remaining bytes in the block
    # otherwise it must be set to block length.
    #
    # @param plain_bytes array containing plain data
    # @param plain_bytes_offset 0-indexed offset from where to start encrypting data
    # @param no_of_bytes_to_encrypt total numbers of bytes to encrypt
    # @param enc_bytes array to receive encrypted data
    # @param enc_bytes_offset 0-indexed offset where to copy encrypted data in enc_bytes
    #
    @abstractmethod
    def encrypt_block(self, plain_bytes: bytearray,
                      plain_bytes_offset: int,
                      no_of_bytes_to_encrypt: int,
                      enc_bytes: bytearray,
                      enc_bytes_offset: int):
        pass

    # Decrypts a single block from enc_bytes starting from
    # enc_bytes_offset and copies it into plain_bytes at plain_bytes_offset.
    #
    # This method decrypts single block only. In case it is a last
    # block, no_of_bytes_to_decrypt should be set to remaining bytes in the block
    # otherwise it must be set to block length.
    #
    # @param enc_bytes array containing encrypted data
    # @param enc_bytes_offset 0-indexed offset from where to start decrypting data
    # @param no_of_bytes_to_decrypt total numbers of bytes to decrypt
    # @param plain_bytes array to receive decrypted data
    # @param plain_bytes_offset 0-indexed offset where to copy decrypted data in plain_bytes
    @abstractmethod
    def decrypt_block(self, enc_bytes: bytearray,
                      enc_bytes_offset: int,
                      no_of_bytes_to_decrypt: int,
                      plain_bytes: bytearray,
                      plain_bytes_offset: int):
        pass

    #
    # Fill the extra padding block in enc_bytes at offset.
    #
    # @param enc_bytes array created to store encrypted data and padding block
    # @param padding_block_offset 0-indexed offset where to copy padding block
    # @param padding_count padding count returned by get_padding_count()
    #
    @abstractmethod
    def fill_padding_block(self, enc_bytes: bytearray,
                           padding_block_offset: int,
                           padding_count: int):
        pass

    #
    # Returns padding count (numbers of bytes to be padded in plain data) based
    # on the size of plain data.
    #
    # @param plain_content_size size of plain data
    # @return returns padding count
    #
    @abstractmethod
    def get_padding_count(self, plain_content_size: int) -> int:
        pass

    #
    # Returns padding count (numbers of bytes are padded in plain data) from
    # the padding information stored in padding block.
    #
    # @param enc_content array containing encrypted data including padding block
    # @param offset_of_padding_block 0-indexed offset at which padding block is stored
    # @return return padding count
    #
    @abstractmethod
    def get_padding_count_from_content(self, enc_content: bytearray, offset_of_padding_block: int) -> int:
        pass


#
# CaesarCipher encrypts and decrypts data using the Caesar cipher. It only
# handles a-z (lower-case) characters.
#
# It is an 8-char block cipher.
#
# The key of the cipher has 8-bytes, each bytes represent the offset/shift for
# respective char in the block.
#
# It uses 'a' as dummy char to fill last-block if data length is not aligned to
# block length.
#
# It fills all chars in padding info block with 'a' + padding_count i.e. if the
# padding_count is 3, all chars in padding blocks are filled with
# 'd' ('a' + 3 = 'd')
#
# Example:
# Key:				  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
# Plain Data:		  | b | b | b | b | b |   |   |   |
# Padded Plain Data:  | b | b | b | b | b | a | a | a |
# Encrypted Data:	  | c | d | e | f | g | g | h | i | d | d | d | d | d | d | d | d |
# 					  |       Data        |  Padding  |          Padding Info         |
#
class CaesarCipher(ICharCipher):
    ZERO_CHAR = ord('a')

    def __init__(self, key: bytearray):
        self.key = key

    @staticmethod
    def key_from_string(key: str) -> bytearray:
        return bytearray([int(keyChar) for keyChar in key])

    def get_block_length(self) -> int:
        return len(self.key)

    def encrypt_block(self, plain_bytes: bytearray,
                      plain_bytes_offset: int,
                      no_of_bytes_to_encrypt: int,
                      enc_bytes: bytearray,
                      enc_bytes_offset: bytearray):
        no_of_bytes_to_encrypt = min(no_of_bytes_to_encrypt, self.get_block_length())

        block_buff = bytearray(self.get_block_length())
        block_buff[0:no_of_bytes_to_encrypt] = plain_bytes[plain_bytes_offset:
                                                           (plain_bytes_offset + no_of_bytes_to_encrypt)]

        if no_of_bytes_to_encrypt < self.get_block_length():
            for i in range(no_of_bytes_to_encrypt, self.get_block_length()):
                block_buff[i] = self.ZERO_CHAR

        for i in range(self.get_block_length()):
            enc_bytes[enc_bytes_offset + i] = self.encrypt_char(block_buff[i], self.key[i])

    def decrypt_block(self, enc_bytes: bytearray,
                      enc_bytes_offset: int,
                      no_of_bytes_to_decrypt: int,
                      plain_bytes: bytearray,
                      plain_bytes_offset: int):
        no_of_bytes_to_decrypt = min(no_of_bytes_to_decrypt, self.get_block_length())
        for i in range(no_of_bytes_to_decrypt):
            plain_bytes[plain_bytes_offset + i] = self.decrypt_char(enc_bytes[enc_bytes_offset + i], self.key[i])

    def fill_padding_block(self, enc_bytes: bytearray,
                           padding_block_offset: int,
                           padding_count: int):
        for i in range(self.get_block_length()):
            enc_bytes[padding_block_offset + i] = (self.ZERO_CHAR + padding_count)

    def get_padding_count(self, plain_content_size: int) -> int:
        if plain_content_size % self.get_block_length() == 0:
            return 0
        else:
            return self.get_block_length() - (plain_content_size % self.get_block_length())

    def get_padding_count_from_content(self, enc_content: bytearray,
                                       offset_of_padding_block: int) -> int:
        return enc_content[offset_of_padding_block] - self.ZERO_CHAR

    @classmethod
    def encrypt_char(cls, ch: int, key: int) -> int:
        return (ch + key - cls.ZERO_CHAR) % 26 + cls.ZERO_CHAR

    @classmethod
    def decrypt_char(cls, ch: int, key: int) -> int:
        return cls.encrypt_char(ch, (26 - key))


#
# Factory class to create instance of ICharCipher.
#
class CharCipherFactory:

    @staticmethod
    def create_caesar_cipher(key: bytearray) -> ICharCipher:
        return CaesarCipher(key)


class EncryptedFileTest:

    ACT_READ = "read"
    ACT_WRITE = "write"
    ACT_GETSIZE = "getSize"
    ACT_SETSIZE = "setSize"
    ACT_ENCRYPT = "encrypt"

    @classmethod
    def test(cls, action: str):
        result = "Incorrect action."
        if action == cls.ACT_READ:
            result = cls.read_test()
        elif action == cls.ACT_WRITE:
            result = cls.write_test()
        elif action == cls.ACT_GETSIZE:
            result = cls.get_size_test()
        elif action == cls.ACT_SETSIZE:
            result = cls.set_size_test()
        elif action == cls.ACT_ENCRYPT:
            result = cls.encrypt_sample()

        print(action)
        print(result)

    @classmethod
    def create_encrypted_file(cls, key: bytearray,
                              content: bytearray) -> IFile:
        return EncryptedFile(MemoryFile(content), CharCipherFactory.create_caesar_cipher(key))

    @classmethod
    def read_test(cls) -> str:
        key = CaesarCipher.key_from_string(input())
        content = bytearray(input(), "utf-8")
        offset = int(input())
        no_of_bytes_to_read = int(input())
        enc_file = cls.create_encrypted_file(key, content)
        bytes_to_read = bytearray(no_of_bytes_to_read)
        read_ret = enc_file.read(offset, no_of_bytes_to_read, bytes_to_read)
        bytes_to_read = bytes_to_read[:read_ret]
        if len(bytes_to_read) > 0 and bytes_to_read[0] != 0:
            return bytes_to_read.decode("utf-8")
        else:
            return "BLANK"

    @classmethod
    def write_test(cls) -> str:
        key = CaesarCipher.key_from_string(input())
        content = bytearray(input(), "utf-8")
        offset = int(input())
        no_of_bytes_to_write = int(input())
        bytes_to_write = bytearray(input(), "utf-8")
        enc_file = cls.create_encrypted_file(key, content)
        enc_file.write(offset, no_of_bytes_to_write, bytes_to_write)
        return enc_file.get_contents().decode("utf-8")

    @classmethod
    def get_size_test(cls) -> str:
        key = CaesarCipher.key_from_string(input())
        content = bytearray(input(), "utf-8")
        enc_file = cls.create_encrypted_file(key, content)
        return str(enc_file.get_size())

    @classmethod
    def set_size_test(cls) -> str:
        key = CaesarCipher.key_from_string(input())
        content = bytearray(input(), "utf-8")
        new_size = int(input())
        enc_file = cls.create_encrypted_file(key, content)
        enc_file.set_size(new_size)
        return enc_file.get_contents().decode("utf-8")

    @classmethod
    def encrypt_sample(cls) -> str:
        key = CaesarCipher.key_from_string(input())
        plain_content = bytearray(input(), "utf-8")
        cipher = CharCipherFactory.create_caesar_cipher(key)
        padding_count = cipher.get_padding_count(len(plain_content))
        enc_content_size = len(plain_content) + padding_count + cipher.get_block_length()
        enc_content = bytearray(enc_content_size)
        for i in range(0, len(plain_content), cipher.get_block_length()):
            remaining_bytes = len(plain_content) - i
            cipher.encrypt_block(plain_content, i,
                                 min(remaining_bytes, cipher.get_block_length()),
                                 enc_content, i)
        cipher.fill_padding_block(enc_content,
                                  len(plain_content) + padding_count,
                                  padding_count)
        return str(enc_content.decode("utf-8"))


class EncryptedFile(IFile):

    def __init__(self, file: IFile,
                 cipher: ICharCipher):
        # TODO: Write code here
        self.file = file
        self.cipher = cipher



    def read(self, offset: int,
             no_of_bytes_to_read: int,
             bytes_read: bytearray) -> int:
        
        # TODO: Write code here
        # (self, offset: int, no_of_bytes_to_read: int, bytes_read: bytearray)
        return self.file.read(offset, no_of_bytes_to_read, bytes_read)

    def write(self, offset: int,
              no_of_bytes_to_write: int,
              bytes_to_write: bytearray) -> int:
        # TODO: Write code here
        return self.file.write(offset, no_of_bytes_to_write, bytes_to_write)

    def set_size(self, new_size: int):
        self.file.set_size

    def get_size(self) -> int:
        d_size = self.file.size
        d_size
        # pass

    def get_contents(self) -> bytes:
        return self.content
        # TODO: Write code here
        pass


# ***************************** Sample Code *********************************
class SampleCode:

    #
    # Sample code to demonstrate encryption of plain data.
    #
    @staticmethod
    def encrypt_sample():
        # your key
        key = bytearray([1, 2, 3, 4, 5, 6, 7, 8])
        # your plain content
        plain_content = bytearray("aaaaaaaaaaaaaaa", "utf-8")

        # create cipher object
        cipher = CharCipherFactory.create_caesar_cipher(key)
        # get no of bytes to pad so content is aligned to block-length
        padding_count = cipher.get_padding_count(len(plain_content))
        # calculate final encrypted content size
        enc_content_size = len(plain_content) + padding_count + cipher.get_block_length()
        enc_content = bytearray(enc_content_size)
        # encrypt content block by block
        for i in range(0, len(plain_content), cipher.get_block_length()):
            remaining_bytes = len(plain_content) - i
            cipher.encrypt_block(plain_content, 
                                 i,
                                 min(remaining_bytes, cipher.get_block_length()),
                                 enc_content, i)
        # fill padding information block
        cipher.fill_padding_block(enc_content,
                                  len(plain_content) + padding_count,
                                  padding_count)
        print("encrypt_sample", enc_content.decode("utf-8"))

    #
    # Sample code to demonstrate decryption of encrypted data.
    #
    @staticmethod
    def decrypt_sample():
        # your key
        key = bytearray([1, 2, 3, 4, 5, 6, 7, 8])
        # your encrypted content
        enc_content = bytearray("bcdefghibcdefghibbbbbbbb", "utf-8")

        # create cipher object
        cipher = CharCipherFactory.create_caesar_cipher(key)
        # get no of bytes padded from padding information block
        padding_count = cipher.get_padding_count_from_content(enc_content, len(enc_content) - cipher.get_block_length())
        # calculate plain content size
        plain_content_size = len(enc_content) - padding_count - cipher.get_block_length()
        plain_content = bytearray(plain_content_size)
        # decrypt content block by block
        for i in range(0, len(plain_content), cipher.get_block_length()):
            remaining_bytes = len(plain_content) - i
            cipher.decrypt_block(enc_content, i,
                                 min(remaining_bytes, cipher.get_block_length()),
                                 plain_content, i)
        print("decrypt_sample", plain_content.decode("utf-8"))

    #
    # Sample code to demonstrate reading data from MemoryFile.
    #
    @staticmethod
    def read_sample():
        try:
            # create file object

            file = MemoryFile(bytearray("abcdefghijklmnopqrstuvwxyz", "utf-8"))
            offset = 0
            buff = bytearray(8)
            while True:
                # read content in chunks
                byte_read = file.read(offset, 8, buff)
                # if there is no more content, finish
                if byte_read == 0:
                    break
                # process data in buff

                # advance the offset
                offset += byte_read
                print("read_sample", buff[0:byte_read].decode("utf-8"))
        except Exception as err:
            print(err)

    #
    # Sample code to demonstrate writing data to MemoryFile.
    #
    @staticmethod
    def write_sample():
        try:
            # crate file object
            file = MemoryFile(bytearray())
            new_content = bytearray("abcdefghijklmnoprstuvwxyz", "utf-8")
            for i in range(0, len(new_content), 8):
                # calculate remaining bytes to be written
                bytes_to_write = min(len(new_content) - i, 8)
                # write content in chunks,
                # we can write whole content in one go also
                file.write(i, bytes_to_write, new_content[i:])
            print("write_sample", file.get_contents().decode("utf-8"))
        except Exception as err:
            print(err)


action_input = input()
EncryptedFileTest.test(action_input)
