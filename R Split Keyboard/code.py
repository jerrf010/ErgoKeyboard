import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.scanners.keypad import KeysScanner, MatrixScanner
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers

holdtap = HoldTap()
layers = Layers()

_KEY_CFG = [
    board.GP7, board.GP4, board.GP11, board.GP10, board.GP5, board.GP1
]

ROW_PINS = (board.GP15, board.GP27, board.GP26, board.GP28, board.GP29)
COL_PINS = (board.GP12, board.GP14, board.GP13)


numLayer = KC.LT(1, KC.SPC)
spcNumLayer = KC.LM(1, KC.LSHIFT)

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()

        self.matrix = [

            MatrixScanner(
                row_pins=ROW_PINS,
                column_pins=COL_PINS,
                columns_to_anodes=DiodeOrientation.COL2ROW,
            ),

            KeysScanner(
                pins=_KEY_CFG,
                value_when_pressed=False,
                pull=True,
            )
        ]

        self.coord_mapping = [
            0,1,2,
            3,4,5,
            6,7,8,
            9,10,11,
            12,13,14,
            
            15,16,17,18,19,20,

            21,22,23,
            24,25,26,
            27,28,29,
            30,31,32,
            33,34,35,
            36,37,38,39,40,41,
        ]

keyboard = MyKeyboard()
keyboard.extensions.append(holdtap)
keyboard.extensions.append(Layers())

keyboard.keymap = [
    [
        KC.T, KC.G, KC.B,
        KC.R, KC.F, KC.V,
        KC.E, KC.D, KC.C,
        KC.W, KC.S, KC.X,
        KC.Q, KC.A, KC.Z,
        KC.LGUI, KC.LSHIFT , KC.SPC, KC.LCTRL, KC.LALT, KC.BSPC,

        KC.Y, KC.H, KC.N,
        KC.U, KC.J, KC.M,
        KC.I, KC.K, KC.COMMA,
        KC.O, KC.L, KC.DOT,
        KC.P, KC.SCOLON, KC.SLASH,
        KC.RGUI, KC.ENTER, KC.LEFT, KC.RIGHT, KC.BSPC, KC.RCTRL,
    ],

    [
        KC.N5, KC.NO, KC.NO,
        KC.N4, KC.NO, KC.NO,
        KC.N3, KC.NO, KC.NO,
        KC.N2, KC.NO, KC.NO,
        KC.N1, KC.NO, KC.NO,
        KC.LGUI, KC.TRNS, KC.TRNS, KC.LCTRL, KC.LALT, KC.BSPC,

        KC.N6, KC.NO, KC.NO,
        KC.N7, KC.NO, KC.NO,
        KC.N8, KC.NO, KC.NO,
        KC.N9, KC.NO, KC.NO,
        KC.N0, KC.NO, KC.NO,
        KC.RGUI, KC.ENTER, KC.LEFT, KC.RIGHT, KC.BSPC, KC.RCTRL,
    ]
]

tx_pin = board.GP8
rx_pin = board.GP9

split = Split(split_type=SplitType.UART, data_pin2=tx_pin, data_pin=rx_pin, uart_flip= False)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go()

