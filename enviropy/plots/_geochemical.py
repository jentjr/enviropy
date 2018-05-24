import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

__all__ = ["piper", "schoeller"]


def piper(title="Piper Plot"):
    """
    Create a Piper plot

    """

    # Basic shape of Piper plot
    offset = 0.05
    offsety = offset * np.tan(np.pi / 3)

    h = 0.5 * np.tan(np.pi / 3)

    ltriangle_x = np.array([0, 0.5, 1, 0])
    ltriangle_y = np.array([0, h, 0, 0])
    rtriangle_x = ltriangle_x + 2 * offset + 1
    rtriangle_y = ltriangle_y

    diamond_x = np.array([0.5, 1, 1.5, 1, 0.5]) + offset
    diamond_y = h * (np.array([1, 2, 1, 0, 1])) + (offset * np.tan(np.pi / 3))

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect="equal", frameon=False, xticks=[], yticks=[])
    ax.plot(ltriangle_x, ltriangle_y, "-k")
    ax.plot(rtriangle_x, rtriangle_y, "-k")
    ax.plot(diamond_x, diamond_y, "-k")

    plt.title(title)
    plt.text(
        -offset,
        -offset,
        u"$Ca^{2+}$",
        horizontalalignment="left",
        verticalalignment="center",
    )
    plt.text(
        0.5,
        h + offset,
        u"$Mg^{2+}$",
        horizontalalignment="center",
        verticalalignment="center",
    )
    plt.text(
        1 + offset,
        -offset,
        u"$Na^+ + K^+$",
        horizontalalignment="right",
        verticalalignment="center",
    )
    plt.text(
        1 + offset,
        -offset,
        u"$HCO_3^- + CO_3^{2-}$",
        horizontalalignment="center",
        verticalalignment="center",
    )
    plt.text(
        1.5 + 2 * offset,
        h + offset,
        u"$SO_4^{2-}$",
        horizontalalignment="center",
        verticalalignment="center",
    )
    plt.text(
        2 + 3 * offset,
        -offset,
        u"$Cl^-$",
        horizontalalignment="right",
        verticalalignment="center",
    )

    plt.show()


def schoeller():
    pass
