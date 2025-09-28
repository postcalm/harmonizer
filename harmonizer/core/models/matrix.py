import copy

from harmonizer.core.models.tuning import Tuning
from harmonizer.core.types.enums.notes import Notes


class Matrix:
    """
    Модель матрицы
    """
    _matrix: list[list]

    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns
        self._init_matrix()

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns

    def transpose(self) -> None:
        """
        Транспонирует матрицу.

        :return: None
        """
        self._matrix = self._transpose()

    def get_transposed(self) -> "Matrix":
        """
        Возвращает новую транспонированную матрицу.

        :return: Матрица
        """
        new = copy.copy(self)
        new.transpose()
        return new

    def _init_matrix(self) -> None:
        self._matrix = [["" for _ in range(self._columns)] for _ in range(self._rows)]

    def _transpose(self) -> list[list]:
        old = self._matrix
        rows = len(self._matrix)
        columns = len(self._matrix[0])
        return [[old[c][r] for c in range(rows)] for r in range(columns)]

    def __getitem__(self, item):
        if isinstance(item, tuple):
            r, c = item
            return self._matrix[r][c]
        return self._matrix[item]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            r, c = key
            self._matrix[r][c] = value
        else:
            self._matrix[key] = value

    def __repr__(self):
        return "\n".join(list(map(str, self._matrix)))


class StringMatrix(Matrix):
    """
    Матрица для построения нот на струнных инструментах, имеющих гриф
    (гитары, укулеле и пр.)
    """

    def __init__(self, tuning: str):
        self._notes = Tuning().get(tuning).notes
        rows = len(self._notes)
        # Больше 13, т.е. 12 ладов + открытые струны (1) нет смысла строить,
        # т.к. после 12 всё повторяется
        columns = 13
        super().__init__(rows, columns)
        self._init()

    def _init(self) -> None:
        for r, n in enumerate(self._notes):
            nn = Notes.get_pretty(n)
            _notes = Notes.get(nn) + [nn]
            for c, note in enumerate(_notes):
                self[r, c] = note
