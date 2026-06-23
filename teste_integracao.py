import ctypes
from bridge import lib, No

def imprimir_no_python(no_ptr):
    if not no_ptr:
        print("Árvore vazia.")
        return
    
    no = no_ptr.contents
    tipo = "Folha" if no.folha else "Interno"
    chaves = [no.chaves[i] for i in range(no.n)]
    print(f"{tipo}: {chaves} | Chaves ocupadas: {no.n}")

# --- TESTE DE INSERÇÃO ---
print("--- Testando Inserção ---")
# Simulando: No* raiz = NULL;
raiz = None 

# No seu C, a função 'inserir' recebe (No* raiz, int chave)
# Como a raiz começa como NULL (None), passamos None no primeiro parâmetro
raiz = lib.inserir(None, 10)
raiz = lib.inserir(raiz, 20)
raiz = lib.inserir(raiz, 5) 

imprimir_no_python(raiz)

# --- TESTE DE BUSCA ---
print("\n--- Testando Busca ---")
# Sua função buscar retorna 1 para true e 0 para false
existe = lib.buscar(raiz, 20)
print(f"Chave 20 encontrada? {'Sim' if existe == 1 else 'Não'}")

# --- TESTE DE REMOÇÃO ---
print("\n--- Testando Remoção ---")
# No seu C: void remover(No** raiz, int chave)
# Passamos o endereço do ponteiro da raiz diretamente
lib.remover(ctypes.byref(raiz), 10)

print("Após remover 10:")
imprimir_no_python(raiz)