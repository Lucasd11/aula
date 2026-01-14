class Livro:

    def __init__(self, titulo: str, autor: str, codigo: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel

    def criar_livro(self, titulo, autor, codigo):
        livro = Livro(titulo, autor, codigo)    
        return livro