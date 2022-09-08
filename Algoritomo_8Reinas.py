""" 
Elaborar un programa para ubicar 8 reainas en un tablero
8 x 8 sin que estas se ataquen entre si  
"""
#%%
""" 
Generamos el tablero  donde las reinas estaran ubicadas
Las reinas se encontraran en un espacio limitado por el indice i y su valor k
La posicion del la reina será Pos_reinas[i] = k
"""




"""
La posicion del la reina 1 será Pos_reinas[i] = k y por comparacion la reina 2 sera Pos_reinas[x] = y
Para limitar las coliciones las condiciones seran i no puede ser igual a x.              (i != x)
Del mismo modo k reina 1 no puede ser igual a (y) reina 2,                               (k != y)
Para la diagonal izq el valor (k-i) de reina 1 no puede ser igual al (y-x) de reina 2,   ((k-i) != (y-x))
Para la diagonal der el valor |(i-x)| no debe ser igual al valor |(k-y)|,  |(i-x)| != |(k-y)|
"""
def comp_pos(k, Pos_reinas, num_reinas):
    cont = 0
    if (cont == k): cont = cont+1
    while cont<num_reinas:
        if (Pos_reinas[cont] == Pos_reinas[k] or abs(cont - k) == abs(Pos_reinas[cont]- Pos_reinas[k]) or (k-Pos_reinas[k]) == (cont - Pos_reinas[cont])):
        #if (cont == k or Pos_reinas[cont] == Pos_reinas[k]):
            return False
        cont = cont+1
    return True


def backtraking(nivel, num_reinas, Pos_reinas ):
    
    if nivel == num_reinas-1:
        print(f"Solucion es ")
        for i in range(num_reinas):
            print(f"({i}, {Pos_reinas[i]}), ")
        return Pos_reinas

    else:
        for k in range(num_reinas):
            Pos_reinas[nivel]=k
            if ( comp_pos(k, Pos_reinas, num_reinas)):
                nivel = nivel + 1
                backtraking(nivel, num_reinas, Pos_reinas)
            



# %%

nivel = 0
num_reinas = 8
Pos_reinas = []
for i in range (8):
    Pos_reinas.append(-10)


# %%
print("inicio")
backtraking(nivel, num_reinas, Pos_reinas)


# %%
