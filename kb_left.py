import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()
    
        self.col_pins = (
            board.GP2,
            board.GP3,
            board.GP4,
            board.GP5,
            board.GP6,
            board.GP7,
            board.GP8,
            board.GP9,
        )

        self.row_pins = (
            board.GP10,
            board.GP11,
            board.GP12,
            board.GP13,
            board.GP14,
        )

        self.diode_orientation = DiodeOrientation.COL2ROW
        
        # Важно!!!
        # К стандартной матрице сканирования добавляем
        # сканирование энкодера. Необходимо правильно указать
        # пины для подключения энкодера в каждом файле (для левой и правой половины).
        # Энкодер и матрица описывается для каждой половины свои.
        # Повороты энкодера будут регистрироваться как нажатия клавиш. По-этому
        # их просто нужно добавить в coord_mapping. В данном случае
        # это 40, 41 и 82, 83. В файле code.py для обеих половин нужно прописать
        # действия на повороты энкодера как нажатия обычных клавиш.
        self.matrix = [
            MatrixScanner(
                column_pins=self.col_pins,
                row_pins=self.row_pins,
            ),
            RotaryioEncoder(
                pin_a=board.GP26,
                pin_b=board.GP27,
                divisor=4,
            ),
        ]

        self.coord_mapping = [
            0,  1,  2,  3,  4,  5,  6,  7,     49, 48, 47, 46, 45, 44, 43, 42,
            8,  9,  10, 11, 12, 13, 14, 15,    57, 56, 55, 54, 53, 52, 51, 50,
            16, 17, 18, 19, 20, 21, 22, 23,    65, 64, 63, 62, 61, 60, 59, 58,
            24, 25, 26, 27, 28, 29, 30, 31,    73, 72, 71, 70, 69, 68, 67, 66,
            32, 33, 34, 35, 36, 37, 38, 39,    81, 80, 79, 78, 77, 76, 75, 74,
            40, 41,                                                    83, 82,
        ]
