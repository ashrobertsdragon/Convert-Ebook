from abc import ABC, abstractmethod
from typing import List

from ._types import SplitType
from .text_conversion import desmarten_text


class BookConversion(ABC):
    def __init__(self, file_path: str, metadata: dict):
        self.file_path: str = file_path
        self.metadata: dict = metadata
        self.book = self._read_file(file_path)

    @abstractmethod
    def _read_file(file_path: str):
        raise NotImplementedError("Must be implemented in child class")

    @abstractmethod
    def split_chapters(self) -> str:
        raise NotImplementedError("Must be implemented in child class")


class ImageExtraction(ABC):
    @abstractmethod
    def extract_images(self) -> List[str]:
        raise NotImplementedError("Must be implemented in child class")


class TextExtraction(ABC):
    @abstractmethod
    def extract_text(self) -> str:
        raise NotImplementedError("Must be implemented in child class")

    @abstractmethod
    def _extract_image_text(self) -> str:
        raise NotImplementedError("Must be implemented in child class")


class ChapterSplit(ABC):
    @abstractmethod
    def __init__(self, text_obj: SplitType, metadata: dict, parent) -> None:
        self.text_obj = text_obj
        self.metadata = metadata
        self.parent = parent

        self.MAX_LINES_TO_CHECK: int = 3
        self.CHAPTER_SEPARATOR: str = "***"

    @abstractmethod
    def split_chapters(self) -> str:
        raise NotImplementedError("Must be implemented in child class")

    def clean_text(self, text: str) -> str:
        """
        Removes smart punctuation from text
        """
        return desmarten_text(text)
