from livros import Livro
from usuarios import Usuario
from emprestimos import Emprestimo

usuario = Usuario("Lucas", "1")
livro = Livro("Biblia", "Deus", "0001")

print(f"Disponibilidade do livro: {livro.disponivel}")

emprestimo = Emprestimo(livro, usuario)

print(f"Empréstimo ativo: {emprestimo.ativo}")
print(f"Disponibilidade do livro: {livro.disponivel}")

Emprestimo.devolver_emprestimo(emprestimo, livro)

print(f"Empréstimo ativo: {emprestimo.ativo}")
print(f"Disponibilidade do livro: {livro.disponivel}")







