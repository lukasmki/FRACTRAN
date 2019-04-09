import sys, os

def execute(n, code, maxOutput):
    """Executes a segment of processed FRACTRAN code."""
    output = [n]
    while len(output) < maxOutput:
        found = False
        for frac in code:
            nf = n*frac[0]
            if nf % frac[1] == 0:
                n = nf // frac[1]
                output.append(n)
                found = True
                break
        if not found:
            break
    return output

def validate(code):
    """Validates unprocessed FRACTRAN code string."""
    n = int(eval(code.split(" ")[0]))
    try:
        maxOutput = int(code.strip().split(" ")[-1])
        code = [[int(eval(a)) for a in c.split("/")] for c in code.split(" ")[1:-1]]
    except:
        maxOutput = 100
        code = [[int(eval(a)) for a in c.split("/")] for c in code.split(" ")[1:]]
    for frac in code:
        if len(frac) != 2:
            print("A FRACTRAN script should be in the form: n n0/d0 n1/d1 n3/d3 ... nk/dk m")
            sys.exit(1)
        for num in frac:
            if num <= 0:
                print("Fractions must be positive.")
                sys.exit(1)
    return n, code, maxOutput

def fractran(code):
    """
    Computes the given FRACTRAN code string given in the form:
        n n0/d0 n1/d1 n3/d3 ... nk/dk m
    Where:
        n is the starting number, and
        m is the max number of output numbers (default 100).
    """
    n, code, maxOutput = validate(code)
    return execute(n, code, maxOutput)

if(__name__=="__main__"):
    try:
        INPUT_FILE = sys.argv[1]
    except:
        INPUT_FILE = input("File destination: ")
    if INPUT_FILE == "":
        code = input("Input FRACTRAN code: ")
        while code != "":
            print(fractran(code))
            code = input("Input FRACTRAN code: ")
        sys.exit(0)
    else:
        with open(os.path.join(sys.path[0], INPUT_FILE), 'r') as file:
            code = file.readline()
    print(fractran(code))