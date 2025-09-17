from abc import ABC, abstractmethod

# Abstract Base Class
class FileHandler(ABC):

    @abstractmethod
    def read(self, filename):
        pass

    @abstractmethod
    def write(self, filename, data):
        pass


# Concrete class for text files
class TextFileHandler(FileHandler):

    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    def write(self, filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"Text written to {filename}")


# Concrete class for binary files
class BinaryFileHandler(FileHandler):

    def read(self, filename):
        with open(filename, "rb") as f:
            return f.read()

    def write(self, filename, data):
        with open(filename, "wb") as f:
            f.write(data)
        print(f"Binary data written to {filename}")


# Example usage
if __name__ == "__main__":
    text_handler = TextFileHandler()
    binary_handler = BinaryFileHandler()

    # Writing text
    text_handler.write("example.txt", "Hello, Python OOP with ABCs!")
    print("Reading text:", text_handler.read("example.txt"))

    # Writing binary
    binary_handler.write("example.bin", b"\x48\x65\x6C\x6C\x6F")
    print("Reading binary:", binary_handler.read("example.bin"))
