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
