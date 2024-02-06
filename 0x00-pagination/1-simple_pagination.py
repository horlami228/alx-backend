import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
            This function takes two interger args
        args:
            page: page number
            page_size: the size of one page

        returns:
            A tuple with the starting index and end index
        """

        first_index = (page - 1) * page_size
        last_index = page_size + first_index

        return first_index, last_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Get the elements for a page number
        """

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        first_index, last_index = self.index_range(page, page_size)

        return self.dataset()[first_index:last_index]
