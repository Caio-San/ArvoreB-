from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ctypes
from bridge import libarvore, No, P

app = FastAPI()

# Configuração de CORS para permitir requisições de qualquer origem (essencial para carregar o index.html localmente)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variável global para manter a árvore na memória do servidor
raiz_ptr = None

def arvore_para_json(ptr):
    if not ptr:
        return None
    
    no = ptr.contents
    # Extraímos as chaves válidas (até o índice n)
    chaves = [no.chaves[i] for i in range(no.n)]
    
    estrutura = {
        "folha": bool(no.folha),
        "n": no.n,
        "chaves": chaves,
        "filhos": []
    }
    
    # Se não for folha, processa os filhos recursivamente
    if not no.folha:
        for i in range(no.n + 1):
            filho = arvore_para_json(no.filhos[i])
            if filho:
                estrutura["filhos"].append(filho)
                
    return estrutura

@app.get("/")
def home():
    return {"status": "API Árvore B+ Online"}

@app.post("/inserir/{valor}")
def inserir_valor(valor: int):
    global raiz_ptr
    # Chama sua função C
    raiz_ptr = libarvore.inserir(raiz_ptr, valor)
    return arvore_para_json(raiz_ptr)

@app.delete("/remover/{valor}")
def remover_valor(valor: int):
    global raiz_ptr
    if raiz_ptr:
        # No seu C, remover recebe No** (passamos o endereço de raiz_ptr)
        libarvore.remover(ctypes.byref(raiz_ptr), valor)
    return arvore_para_json(raiz_ptr)

@app.get("/visualizar")
def visualizar():
    return arvore_para_json(raiz_ptr)