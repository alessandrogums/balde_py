import math 


def balde(max_a,max_b,vol_a,vol_b,valor_esperado,vol_transf=0):
    print(f'o volume do balde A é {vol_a}, já o do balde B é {vol_transf}')
    if max_a==valor_esperado or max_b==valor_esperado:
        return vol_a,vol_b
    if vol_transf==valor_esperado or vol_transf-vol_b == valor_esperado or max_a-max_b==valor_esperado:
        return vol_a,vol_b
        
    else:
        qte=math.ceil(vol_a/max_b)
        vol_transf=(qte*(max_b)) % vol_a
        return balde(max_a,max_b,max_a - vol_transf,vol_b,valor_esperado,vol_transf)


print(balde(33,12,33,12,1))