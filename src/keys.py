import os
from yaml import safe_load

def tokens():
    PATH = '../key.yaml'  # arquivo em formato string e não dicionario 

    with open(PATH) as token_f:
        # token_data é o dicionário carregado do YAML
        token_data = safe_load(token_f) 
    
    # [CORREÇÃO 1] Extrair a string do dicionário
    # Vamos garantir que é uma string
    token_string = str(token_data)

    # [CORREÇÃO 1 - Continuação] Atribuir a STRING à variável de ambiente
    os.environ['HUGGING_API_TOKEN'] = token_string

    print(f">>>TOKEN ACESSADO COM SUCESSO<<")
    
    # Vamos verificar se o OS "aprendeu" a variável (apenas dentro deste script)
    print("Verificando a variável no os.environ:")
    
    # print(os.getenv("HUGGING_API_TOKEN"))
    

