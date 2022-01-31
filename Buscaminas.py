#!/usr/bin/env python
# coding: utf-8

# In[333]:


import numpy as np
import random as rn


# In[334]:


def pedido_dimension_usuario():
    
    return int(input('Ingrese la dimension de su matriz: '))


# In[335]:


def pedido_nro_minas(dim):
    
    print('Ingrese el numero de minas menor o igual a', dim-int (dim/3)) 
    
    return int(input())


# In[336]:


def crear_matriz(dim):
    M = [['-' for x in range(dim)]for y in range(dim)]
    
    return(M)


# In[337]:


def asignar_minas(M,dim,max_minas):
    
    nro_minas = 0
    pos_minas_c = np.arange(0,max_minas)
    pos_minas_f = np.arange(0,max_minas)
    
    while(nro_minas != max_minas):
        
        for f in range(dim):
            for c in range(dim):
                M[f][c] = '-'
        
        nro_minas = 0
        
        for i in range(max_minas):
            pos_minas_c[i] = rn.randint(0,dim-1)
            pos_minas_f[i] = rn.randint(0,dim-1)
            

        for m in range(max_minas):
            M[pos_minas_c[m]][pos_minas_f[m]] = 'x'
        
        for f in range(dim):
            for c in range(dim):
                if (M[f][c] == 'x') and (nro_minas!=max_minas):
                    nro_minas+=1
        #print('Check minas: ',nro_minas)
        
                 
    #print(pos_minas_c)
    #print(pos_minas_f)
    
    return M


# In[338]:


def asignacion_valores(M,dim):
    s="" 
    for i in range(dim):
        for j in range(dim):
            if(M[i][j]!='x'):
                cant_minas = 0
                if((dim-1>=i-1>=0)and(dim-1>=j-1>=0)):
                    if(M[i-1][j-1]=='x'):
                        cant_minas+=1
                if(dim-1>=j-1>=0):
                    if(M[i][j-1]=='x'):
                        cant_minas+=1
                if(dim-1>=i-1>=0):
                    if(M[i-1][j]=='x'):
                        cant_minas+=1
                if((dim-1>=i+1>=0) and (dim-1>=j-1>=0)):
                    if(M[i+1][j-1]=='x'):
                        cant_minas+=1
                if((dim-1>=i-1>=0) and (dim-1>=j+1>=0)):
                    if(M[i-1][j+1]=='x'):
                        cant_minas+=1
                if(dim-1>=i+1>=0):
                    if(M[i+1][j]=='x'):
                        cant_minas+=1
                if(dim-1>=j+1>=0):
                    if(M[i][j+1]=='x'):
                        cant_minas+=1
                if((dim-1>=i+1>=0) and (dim-1>=j+1>=0)):
                    if(M[i+1][j+1]=='x'):
                        cant_minas+=1
                if(cant_minas>0):
                    M[i][j]=cant_minas

    for fil in range(dim):
        for col in range(dim):
            s+=str(M[fil][col])+ '\t'
        print(s)
        s=""   
        
    return M


# In[340]:


dim = pedido_dimension_usuario()
M = crear_matriz(dim)
M = asignar_minas(M,dim,pedido_nro_minas(dim))
M = asignacion_valores(M,dim)


# In[341]:


def mostrar_matriz(M):
    s="" 
    for fil in range(dim):
        for col in range(dim):
            s+=str(M[fil][col])+ '\t'
        print(s)
        s=""   


# In[355]:


fin = 0

M_aux = [['.' for x in range(dim)]for y in range(dim)]

while (fin != 1):
    
        print('Ingrese las coordenadas comprendidas entre 0 y',dim)
        columna_selec = int(input('Coordenada X:'))
        fila_selec = int(input('Coordenada Y:'))
        
        if (M[fila_selec][columna_selec] == 'x'):
            print('PERDEDOR')
            mostrar_matriz(M)
            fin = 1
        else:
            if (M[fila_selec][columna_selec] != '-'):
                M_aux[fila_selec][columna_selec] = M[fila_selec][columna_selec]
                mostrar_matriz(M_aux)
            else:
                col = columna_selec
                fila = fila_selec
                
                M_aux[fila][col] = M[fila][col]
                
                #Para abajo
                
                while(M[fila][col] == '-'):
                    
                    M_aux[fila][col] = M[fila][col]
                    
                    if(fila<=dim-1):
                        while(M[fila][col] == '-') and (fila<=dim-1):
                            M_aux[fila][col] = M[fila][col]
                            fila+=1
                            print('fila 1',fila)
                            
                            if(fila==dim-1):
                                break
                            M_aux[fila][col] = M[fila][col]

                    fila = fila_selec
                        
                     
                    if(fila>0):
                        while(M[fila][col] == '-') and (fila>=0):
                            M_aux[fila][col] = M[fila][col]
                            fila-=1
                            print('fila 2',fila)
                            if(fila<0):
                                break
                            M_aux[fila][col] = M[fila][col]

                    fila = fila_selec
                    col+=1

                    print('col 1',col)

                    if(col>=dim):
                        break

                    M_aux[fila][col] = M[fila][col]
                        
                col = columna_selec
                fila = fila_selec
                    
                #Para arriba
                while(M[fila][col] == '-'):
                    
                    M_aux[fila][col] = M[fila][col]
                    
                    if(fila<=dim-1):
                        while(M[fila][col] == '-') and (fila<=dim-1):
                            M_aux[fila][col] = M[fila][col]
                            fila+=1
                            print('fila 3',fila)
                            if(fila==dim):
                                break        
                            M_aux[fila][col] = M[fila][col]
                
                    fila = fila_selec

                    if(fila>0):
                        while(M[fila][col] == '-') and (fila>=0):
                            M_aux[fila][col] = M[fila][col]
                            fila-=1
                            print('fila 4',fila)
                            if(fila<0):
                                break
                            M_aux[fila][col] = M[fila][col]
                        
                    fila = fila_selec
                    col-=1
                    
                    print('col 2',col)
                        
                    if(col<0):
                        break
                        
                    M_aux[fila][col] = M[fila][col]
                    
                col = columna_selec
                fila = fila_selec
                
                #--------------Inverso--------------
                
                M_aux[fila][col] = M[fila][col]
                
                #Para abajo
                
                while(M[fila][col] == '-'):
                    
                    M_aux[fila][col] = M[fila][col]
                    
                    if(col<=dim-1):
                        while(M[fila][col] == '-') and (col<=dim-1):
                            M_aux[fila][col] = M[fila][col]
                            col+=1
                            print('col 1',col)
                            
                            if(col==dim-1):
                                break
                            M_aux[fila][col] = M[fila][col]

                    col = columna_selec
                        
                     
                    if(col>0):
                        while(M[fila][col] == '-') and (col>=0):
                            M_aux[fila][col] = M[fila][col]
                            col-=1
                            print('col 2',col)
                            if(col<0):
                                break
                            M_aux[fila][col] = M[fila][col]

                    col = columna_selec
                    fila+=1

                    print('fila 1',fila)

                    if(fila>=dim):
                        break

                    M_aux[fila][col] = M[fila][col]
                        
                col = columna_selec
                fila = fila_selec
                    
                #Para arriba
                while(M[fila][col] == '-'):
                    
                    M_aux[fila][col] = M[fila][col]

                    if(col<=dim-1):
                        while(M[fila][col] == '-') and (col<=dim-1):
                            M_aux[fila][col] = M[fila][col]
                            col+=1
                            print('col 3',col)
                            
                            if(col==dim-1):
                                break
                            M_aux[fila][col] = M[fila][col]

                    col = columna_selec  
                     
                    if(col>0):
                        while(M[fila][col] == '-') and (col>=0):
                            M_aux[fila][col] = M[fila][col]
                            col-=1
                            print('col 4',col)
                            if(col<0):
                                break
                            M_aux[fila][col] = M[fila][col]
                    
                    col = columna_selec
                    fila-=1
                    
                    print('fila 2',fila)
                        
                    if(col<0):
                        break
                        
                    M_aux[fila][col] = M[fila][col]
                    
                col = columna_selec
                fila = fila_selec
                
                mostrar_matriz(M_aux)


# In[ ]:





# In[ ]:





# In[ ]:




