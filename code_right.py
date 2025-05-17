import board
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap
from kmk.modules.holdtap import HoldTap
from kmk.modules.split import Split, SplitSide, SplitType
from myconf import MYPASSW


# Filler keys
_____ = KC.TRNS  # прозрачные клавиши
xxxxx = KC.NO    # незанятые клавиши
ooooo = KC.NO    # отсутствующие клавиши
zzzzz = KC.NO    # энкодер

keyboard = KMKKeyboard()
# encoder_handler = EncoderHandler()
layers = Layers()
mediakeys = MediaKeys()
holdtap = HoldTap()
macros = Macros()

split = Split(
        split_flip=True,
        split_side=SplitSide.RIGHT,
        split_type=SplitType.UART,
        # split_target_left=True,
        uart_interval=20,
        data_pin=board.GP0,
        data_pin2=board.GP1,
        uart_flip=True,
        use_pio=True,
    )

keyboard.debug_enabled = False

keyboard.modules = [layers, macros, holdtap, mediakeys, split]

# my keys
SPCSHIFT = KC.HT(KC.SPC, KC.LSFT)  # пробел или шифт
MCOPY = KC.LCTL(KC.INS)     # копировать
MPASTE = KC.LSFT(KC.INS)    # вставить
CTRLSHIFT = KC.LSFT(KC.LCTL)  # ctrl + shift

#### МАКРОСЫ ####
# печатает пароль
macros = Macros()
PASSW = KC.MACRO(
    MYPASSW,
    Tap(KC.ENTER),
)

# Layers
FN = KC.MO(1)
FS = KC.MO(2)

keyboard.keymap = [
    # базовый слой
    # энкодер на левой половине будет уменьшать/увеличивать громкость (KC.VOLD, KC.VOLU)
    # на правой половине - стрелки вправо/влево (KC.RIGHT, KC.LEFT)
    [
        KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,   ooooo,     ooooo,     ooooo,   ooooo,    KC.N6,   KC.N7, KC.N8,    KC.N9,  KC.N0,    KC.RBRC,
        KC.TAB,  KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,    ooooo,     ooooo,     ooooo,   ooooo,    KC.Y,    KC.U,  KC.I,     KC.O,   KC.P,     KC.LBRC,
        KC.CAPS, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,    CTRLSHIFT, ooooo,     ooooo,   KC.BSPC,  KC.H,    KC.J,  KC.K,     KC.L,   KC.SCLN,  KC.QUOT,
        KC.LCTL, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,    KC.BSLS,   MCOPY,     MPASTE,  KC.INS,   KC.N,    KC.M,  KC.COMMA, KC.DOT, KC.SLSH,  KC.ENT,
        ooooo,   ooooo, ooooo, ooooo, FN,    KC.LGUI, SPCSHIFT,  KC.EQL,    KC.MINS, SPCSHIFT, KC.LALT, FS,    ooooo,    ooooo,  ooooo,    ooooo,
        KC.VOLD, KC.VOLU,                                                                                                        KC.RIGHT, KC.LEFT,
    ],
    # FN
    [
        _____, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, ooooo, ooooo,        ooooo, ooooo, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx,
        _____, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, ooooo, ooooo,       ooooo, ooooo, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx,
        _____, KC.F11, KC.F12, xxxxx, xxxxx, xxxxx, xxxxx, ooooo,      ooooo, KC.DEL, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx,
        _____, KC.HOME, KC.END, MCOPY, MPASTE, xxxxx, xxxxx, zzzzz,    zzzzz, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, _____,
        ooooo, ooooo, ooooo, ooooo, _____, _____, _____, _____,        _____, _____, PASSW, _____, ooooo, ooooo, ooooo, ooooo,
        zzzzz,   zzzzz,                                                                                          zzzzz, zzzzz,
    ],
    # FS
    [
        _____, xxxxx,   xxxxx,   xxxxx,    xxxxx, xxxxx, ooooo, ooooo,        ooooo, ooooo, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx,
        _____, xxxxx,   KC.UP,   xxxxx,    xxxxx, xxxxx, ooooo, ooooo,        ooooo, ooooo, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx,
        _____, KC.LEFT, KC.DOWN, KC.RIGHT, KC.F3, KC.F4, xxxxx, ooooo,        ooooo, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.GRV,
        _____, xxxxx,   xxxxx,   xxxxx,    xxxxx, xxxxx, xxxxx, zzzzz,        zzzzz, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, _____,
        ooooo, ooooo, ooooo, ooooo, _____, _____, _____, _____,               _____, _____, _____, _____, ooooo, ooooo, ooooo, ooooo,
        zzzzz,   zzzzz,                                                                                               zzzzz,   zzzzz,
    ],

]


if __name__ == '__main__':
    keyboard.go()
