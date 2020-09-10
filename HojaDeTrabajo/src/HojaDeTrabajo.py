tk_parA = "("
tk_parC = ")"
tk_menorQ = "<"
tk_mayorQ = ">"
tk_corchA = "["
tk_corchC = "]"
tk_igual = "="
tk_coma = ","

archivo = """(
    <
    [precio] = 45.09,
    [descripcion] = "adios mundo",
    [disponible] = false
    >,
    <
    [precio] = 4,
    [descripcion] = "adios mundo",
    [disponible] = false
    >,
    <
    [precio] = -56.4,
    [descripcion] =  "este es el otro ejemplo, las cadenas pueden ser muy largas",
    [disponible] = false
    >
)"""
archivo = archivo.replace(" ", "")
archivo = archivo.replace("\n", "")
archivo = archivo.replace("\t", "")


def AFD (entrada):
    estado = 0
    print(entrada)
    for i in range(len(entrada)):
        encurso = entrada[i]
        try:
            siguiente = entrada[i+1]
        except:
            pass
        if encurso == tk_parA and estado == 0:
            print('tk_parA')
            estado = 1
        elif encurso == tk_menorQ and estado == 1:
            print('tk_menorQ')
            estado = 2
        elif encurso == tk_corchA and estado == 2:
            print('tk_corchA')
            estado = 3
        elif encurso.isalpha() and estado == (3 or 2):
            if estado == 3:
                print('tk_palabra')
                estado = 2
        elif encurso.isdigit() and estado == 3:
            print('tk_numero')
            estado = 2
        elif encurso == tk_corchC and estado == 2:
            print('tk_corchC')
            estado = 3
        elif encurso == tk_mayorQ and estado == 1:
            print('tk_mayorQ')
            estado = 1
        elif encurso == tk_parC and estado == 1:
            return print('tk_parC')
        elif (encurso == tk_coma or encurso == '"') and (entrada[i + 1] == tk_menorQ or entrada[i + 1] == tk_corchA):
            if entrada[i + 1] == tk_mayorQ or entrada[i+1] == tk_menorQ:
                estado = 1
            else:
                estado = 2
        if encurso.isalpha() and siguiente == tk_mayorQ:
            estado = 1


AFD(archivo)
