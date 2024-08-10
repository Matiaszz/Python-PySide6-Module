
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)
import qdarkstyle


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    app.setStyleSheet(app.styleSheet() + qss)
