from rich.traceback import install
install()

def divisao(x=0,y=1):
    div = x/y
    if int(x/y) - x/y == 0:
        div = int(div)
    return div

print(divisao(0,0))