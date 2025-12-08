import pandas as pd
from pathlib import Path


class DataGetter:
    """Fetch file data by name from a fixed base path."""

    def __init__(self, base_path: str = ".") -> None:
        self._base_path = Path(base_path)

    def read_file(self, file_name: str, encoding: str = "utf-8") -> str:
        """Read a text file and return its content."""
        file_path = self._base_path / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"'{file_name}' not found in '{self._base_path}'")
        return file_path.read_text(encoding=encoding)

    def read_csv(self, file_name: str) -> pd.DataFrame:
        """Read a CSV file and return a DataFrame."""
        file_path = self._base_path / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"'{file_name}' not found in '{self._base_path}'")
        return pd.read_csv(file_path)

    def __repr__(self) -> str:
        return f"<DataGetter base_path='{self._base_path}'>"


