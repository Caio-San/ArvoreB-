import ctypes
import sys

# 1. Definição das constantes (devem ser iguais ao seu arvoreB.h)
P = 3
PFOLHA = 2

# 2. Classe que espelha a struct No do C
class No(ctypes.Structure):
    pass

# Definindo os campos da struct conforme seu arquivo arvoreB.h
No._fields_ = [
    ("folha", ctypes.c_int),          # int folha
    ("n", ctypes.c_int),              # int n
    ("chaves", ctypes.c_int * P),     # int chaves[P]
    ("filhos", ctypes.POINTER(No) * (P + 1)), # No* filhos[P + 1]
    ("prox", ctypes.POINTER(No))      # No* prox
]

# 3. Carregar a biblioteca compilada
lib_name = "./libarvore.dll" if sys.platform.startswith("win") else "./libarvore.so"
lib = None
try:
    lib = ctypes.CDLL(lib_name)
except OSError:
    try:
        lib = ctypes.CDLL(lib_name.lstrip("./"))
    except OSError:
        print(f"Erro: Não encontrou {lib_name}. Compile o C primeiro!")

# Alias para manter compatibilidade com api.py
libarvore = lib

# 4. Configurar os tipos de retorno das funções principais
if lib:
    lib.inserir.restype = ctypes.POINTER(No)      # Retorna No*
    lib.remover.argtypes = [ctypes.POINTER(ctypes.POINTER(No)), ctypes.c_int] # Recebe No** e int
    lib.buscar.restype = ctypes.c_int             # Retorna int (0 ou 1)