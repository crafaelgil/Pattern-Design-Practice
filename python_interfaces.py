class InformalParserInterface:
  def load_data_source(self, path: str, file_name: str) -> str:
    """Loads in file for extracting text"""
    pass

  def extract_text(self, full_file_name: str) -> dict:
    """Extracts text from the current file"""
    pass
