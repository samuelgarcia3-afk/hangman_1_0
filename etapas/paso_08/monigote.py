"""Etapas del dibujo del ahorcado. ETAPAS[0] = 1er error ... ETAPAS[5] = 6to error."""

_BASE = [
    "  ┌───┐  ",
    "  │   {0}  ",
    "  │  {1}{2}{3} ",
    "  │  {4} {5} ",
    "  │       ",
    "──┴──     ",
]

def _armar(cabeza=" ", torso=" ", brazo_i=" ", brazo_d=" ", pie_i=" ", pie_d=" "):
    return "\n".join(l.format(cabeza, brazo_i, torso, brazo_d, pie_i, pie_d) for l in _BASE)

ETAPAS = [
    _armar("O"),
    _armar("O", "|"),
    _armar("O", "|", "/"),
    _armar("O", "|", "/", "\\"),
    _armar("O", "|", "/", "\\", "/"),
    _armar("O", "|", "/", "\\", "/", "\\"),
]
