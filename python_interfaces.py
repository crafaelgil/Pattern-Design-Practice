import abc

class InformalParserInterface:
  def load_data_source(self, path: str, file_name: str) -> str:
    """Loads in file for extracting text"""
    pass

  def extract_text(self, full_file_path: str) -> dict:
    """Extracts text from the current file"""
    pass

class PDFParser(InformalParserInterface):
  def load_data_source(self, path: str, file_name: str) -> str:
      return super().load_data_source(path, file_name)

  def extract_text(self, full_file_path: str) -> dict:
      return super().extract_text(full_file_path)

class EmailParser(InformalParserInterface):
  def load_data_source(self, path: str, file_name: str) -> str:
      return super().loadclea_data_source(path, file_name)

  def extract_text_from_email(self, full_file_path: str) -> dict:
      pass

# print(issubclass(PDFParser, InformalParserInterface))
# print(issubclass(EmailParser, InformalParserInterface))

class ParserMeta(type):
  def __instancecheck__(cls, instance):
    return cls.__subclasscheck__(type(instance))

  def __subclasscheck__(cls, subclass):
    return (hasattr(subclass, 'load_data_source') and
            callable(subclass.load_data_source) and
            hasattr(subclass, 'extract_text') and
            callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
  pass

class PDFParserNew:
  def load_data_source(self, path: str, file_name: str) -> str:
    pass

  def extract_text(self, full_file_path: str) -> dict:
    pass

class EmailParserNew:
  def load_data_source(self, path: str, file_name: str) -> str:
    pass

  def extract_text_from_email(self, full_file_path: str) -> dict:
    pass

# print(issubclass(PDFParserNew, UpdatedInformalParserInterface))
# print(issubclass(EmailParserNew, UpdatedInformalParserInterface))

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

print(issubclass(PDFParserNew, UpdatedInformalParserInterface))
print(issubclass(EmailParserNew, UpdatedInformalParserInterface))
