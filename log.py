import os

def funcLog (messagem): 
    ju_var = os.environ.get('JR_VAR')
    print (ju_var)
    print ("Adicionando um log.", messagem)