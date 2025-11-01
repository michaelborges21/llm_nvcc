import torch 

def processador():
    
    process = "cuda" if torch.cuda.is_available() else "cpu"
    props = torch.cuda.get_device_properties(0)
    
    print(f"Nome: {props.name}")
    print(f"Total de memória: {props.total_memory / 1024**3:.2f} GB")
    print(f"Multiprocessadores: {props.multi_processor_count}")
    print(f"Capacidade de computação: {props.major}.{props.minor}\n")
    print(f"Trabalhando com: {process}\n")

    return process