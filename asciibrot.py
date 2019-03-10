# code golf: generating a Mandelbrot set in ASCII

# Height and Width of terminal
H = 40
W = 80

def coord_to_complex(i, j):
    """ map the region [0,H)x[0,W) into the 
    complex plane """
    re = float(4*i)/float(W-1) - 2.0   # real component
    im = float(2.2*j)/float(H-1) - 1.1   # imaginary component
    # return complex number as order pair of reals
    return (re,im)

def is_in_mandelbrot(re, im):
    # this is fixed over the iteration
    cr = re; ci = im
    zr = cr; zi = ci
    from math import sqrt
    for t in range(1000):
        zr = (zr**2 - zi**2) + cr
        zi = 2*zi*zr         + ci
        if sqrt(zr**2 + zi**2) > 2:
            return False
    # if the complex number re + i(im) made it this far without 
    # growing beyond modulus 2, then it is (probably) in the 
    # Mandelbrot set (or diverging slowly)
    return True

def show_set():
    ln = ""
    for i in range(H):
        for j in range(W):
            if is_in_mandelbrot(coord_to_complex(j,i)):
                ln += "*"
            else:
                ln += " "
        ln += "\n"
    print(ln)
        
show_set()