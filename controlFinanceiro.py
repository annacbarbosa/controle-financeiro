class Despesa:
    def __init__(self, categoria, valor):
        self.categoria = categoria
        self.valor = valor

class Receita:
    def __init__(self, fonte, valor):
        self.fonte = fonte
        self.valor = valor

class Conta:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.receitas = []
        self.despesas = []

    def adicionar_receita(self, fonte, valor):
        self.receitas.append(Receita(fonte, valor))
        self.saldo += valor

    def adicionar_despesa(self, categoria, valor):
        self.despesas.append(Despesa(categoria, valor))
        self.saldo -= valor

    def extrato(self):
        extrato = []
        saldo_atual = self.saldo
        for receita in self.receitas:
            extrato.append(f"Receita: {receita.fonte} - R${receita.valor:.2f} (Saldo: R${saldo_atual:.2f})")
            saldo_atual += receita.valor
        for despesa in self.despesas:
            extrato.append(f"Despesa ({despesa.categoria}): R${despesa.valor:.2f} (Saldo: R${saldo_atual:.2f})")
            saldo_atual -= despesa.valor
        return extrato

    def relatorio_gastos_por_categoria(self):
        categorias = {}
        for despesa in self.despesas:
            if despesa.categoria in categorias:
                categorias[despesa.categoria] += despesa.valor
            else:
                categorias[despesa.categoria] = despesa.valor
        return sorted(categorias.items(), key=lambda x: x[1], reverse=True)

    def relatorio_receitas(self):
        return [(receita.fonte, receita.valor) for receita in self.receitas]

def menu():
    print("\nSISTEMA DE GASTOS FINANCEIROS")
    print("1. Adicionar Despesa")
    print("2. Mostrar Extrato")
    print("3. Mostrar Gastos por Categoria")
    print("4. Mostrar Receitas")
    print("0. Sair")

def adicionar_despesa(conta):
    categoria = input("Digite a categoria da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    conta.adicionar_despesa(categoria, valor)
    print("Despesa adicionada com sucesso!")

def mostrar_extrato(conta):
    print("\nExtrato:")
    for linha in conta.extrato():
        print(linha)

def mostrar_gastos_por_categoria(conta):
    print("\nGastos por Categoria:")
    for categoria, valor in conta.relatorio_gastos_por_categoria():
        print(f"{categoria}: R${valor:.2f}")

def mostrar_receitas(conta):
    print("\nReceitas:")
    for fonte, valor in conta.relatorio_receitas():
        print(f"{fonte}: R${valor:.2f}")

def main():
    saldo_inicial = float(input("Digite seu saldo inicial: "))
    conta = Conta(saldo_inicial)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_despesa(conta)
        elif opcao == "2":
            mostrar_extrato(conta)
        elif opcao == "3":
            mostrar_gastos_por_categoria(conta)
        elif opcao == "4":
            mostrar_receitas(conta)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
