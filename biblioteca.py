class biblioteca:
    def listar_usuarios(self):
        if not self.usuarios:
            print("Não há usuários")
        else:
            for usuario in self.usuarios