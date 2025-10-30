import os
from yaml import safe_load

def tokens()->str:
    PATH = '../key.yaml'  # arquivo em formato string e não dicionario 

    with open(PATH) as token_f:
        # token_data é o dicionário carregado do YAML
        token_data = safe_load(token_f) 
    
    # Extrair a string do dicionário
    token_string = token_data['TOKEN']
   
    # Atribuir a STRING à variável de ambiente
    os.environ['TOKEN'] = token_string
    
    print(f">>>TOKEN ACESSADO COM SUCESSO<<")
    
    T = token_string[0:8]
    return T