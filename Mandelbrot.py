import matplotlib.pyplot as plt 

def compl_mult (a,b):
    
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def compl_add (a,b):
    
    return (a[0] + b[0], a[1] + b[1])
 
def verif_ab (a,b):
    
    B = False
    i = 200
    z = (0,0)
     
    for k in range(i):
         
        z = compl_add(compl_mult(z,z),(a,b))
         
    if z[0]*z[0]+z[1]*z[1] < 4:
        
        B = True
        
    return B

def plot():
    
    a = 200 #Nombre de points pour dessiner l'ensemble (à abaisser si le script est trop lent)
    
    plt.axis([-2.1,0.6,-1.2,1.2])
    plt.grid()
    
    for i in range (a):
        
        for j in range (a):
            
            if verif_ab(2.7*(i/a)-2.1,2.4*(j/a)-1.2):
    
                plt.plot(2.7*(i/a)-2.1,2.4*(j/a)-1.2, 'r,')
    
    plt.show()

plot()
