def newton(f, fd, x0, tol, max_iter): # Přidal jsem 'fd' jako druhý parametr
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fdx = fd(x) # Derivace
        
        if abs(fdx) < 1e-12: # Ochrana proti dělení nulou
            return None
            
        x_new = x - fx / fdx
        
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x