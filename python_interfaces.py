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
      return super().load_data_source(path, file_name)

  def extract_text_from_email(self, full_file_path: str) -> dict:
      pass

print(issubclass(PDFParser, InformalParserInterface))
print(issubclass(EmailParser, InformalParserInterface))

class ParserMeta(type):
  def __instancecheck__(cls, instance):
    return cls.__subclasscheck__(type(instance))

  def __subclasscheck__(cls, subclass):
    return (hasattr(subclass, 'load_data_source') and
            callable(subclass.load_data_source) and
            hasattr(subclass, 'extract_text') and
            callable(subclass.extract_text))

def UpdatedInformalParserInterface(metaclass=ParserMeta):
  pass
