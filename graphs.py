# plots.py
import matplotlib.pyplot as plt

def plot_vector(x_vals, title="Složky vektoru x"):
    """x_i vs i (i=1..N)"""
    i_vals = list(range(1, len(x_vals) + 1))
    plt.figure()
    plt.plot(i_vals, x_vals, "o-")
    plt.xlabel("i")
    plt.ylabel("x_i")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_scatter(x, y, title="Data"):
    """bodový graf (data)"""
    plt.figure()
    plt.plot(x, y, "o")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_compare(x_data, y_data, x_line, y_line, title="Data vs křivka",
                 data_label="data", line_label="model/interpolace"):
    """data + jedna křivka v jednom grafu"""
    plt.figure()
    plt.plot(x_data, y_data, "o", label=data_label)
    plt.plot(x_line, y_line, "-", label=line_label)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_error_i(y_vals, i_start=1, title="y(i) = I_N(i) - I_A"):
    """chyba y(i) vs i"""
    i_vals = list(range(i_start, i_start + len(y_vals)))
    plt.figure()
    plt.plot(i_vals, y_vals, "o-")
    plt.axhline(0)
    plt.xlabel("i")
    plt.ylabel("y(i)")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_abs_error_log(y_vals, i_start=1, title="|y(i)|"):
    """log graf absolutní chyby (stabilita/zaokrouhlení)"""
    i_vals = list(range(i_start, i_start + len(y_vals)))
    abs_err = [abs(v) for v in y_vals]
    plt.figure()
    plt.semilogy(i_vals, abs_err, "o-")
    plt.xlabel("i")
    plt.ylabel("|y(i)|")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_matrix_heatmap(A, title="Matice A"):
    """vizualizace matice (heatmap)"""
    plt.figure()
    plt.imshow(A, aspect="auto")
    plt.title(title)
    plt.colorbar()
    plt.show()

def plot_timeseries(t, y, title="Časová řada", y_label="y(t)"):
    """ODR: průběh v čase"""
    plt.figure()
    plt.plot(t, y, "-")
    plt.xlabel("t")
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

print("graphs.py loaded.")