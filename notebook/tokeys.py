from yaml import safe_load

def keys():
    PATH = 'key.yaml'
    with open(PATH) as token_file:
        token  = safe_load(token_file)
    os.environ['HUGGING_API_TOKEN'] = token['HUGGING_API_TOKEN']
    
    