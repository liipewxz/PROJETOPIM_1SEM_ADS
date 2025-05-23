import json
import os
import random

ARQUIVO = "usuarios_lgpd.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_dados(lista):
    with open(ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)

cursos_disponiveis = [
    "Lógica",
    "Segurança Digital",
    "Introdução à Programação",
    "Redes de Computadores",
    "Banco de Dados",
    "Empreendedorismo Digital"
]

medidas_lgpd = [
    "1. Coleta mínima de dados necessários.",
    "2. Consentimento do usuário ao se cadastrar.",
    "3. Dados não serão compartilhados com terceiros.",
    "4. Acesso protegido por senha.",
    "5. Criptografia de senhas (simulada).",
    "6. Possibilidade de alteração de senha.",
    "7. Verificação de duas etapas no login.",
    "8. Backup regular dos dados (sugestão para ONG).",
    "9. Direito de exclusão dos dados (LGPD).",
    "10. Informações claras sobre o uso dos dados."
]

def exibir_medidas_lgpd():
    print("\n--- Medidas de Segurança LGPD ---")
    for item in medidas_lgpd:
        print(item)
    input("\nPressione Enter para retornar ao menu...")

def registrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("\nCursos disponíveis:")
    for i, curso in enumerate(cursos_disponiveis, 1):
        print(f"{i}. {curso}")
    opcao = int(input("Escolha o número do curso: "))
    curso = cursos_disponiveis[opcao - 1]

    nota = float(input("Nota final (0 a 10): "))
    senha = input("Crie uma senha (mínimo 6 caracteres): ")

    if len(senha) < 6:
        print("⚠️ Senha fraca. Operação cancelada.")
        return

    status = "Aprovado" if nota >= 7 else "Reprovado"

    usuario = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota": nota,
        "status": status,
        "senha": senha
    }

    dados = carregar_dados()
    dados.append(usuario)
    salvar_dados(dados)
    print("✅ Usuário cadastrado com sucesso!")

def mostrar_usuarios():
    print("\n--- Lista de Usuários ---")
    dados = carregar_dados()
    for u in dados:
        print(f"Nome: {u['nome']} | Curso: {u['curso']} | Nota: {u['nota']} | Status: {u['status']}")

def calcular_media():
    dados = carregar_dados()
    if not dados:
        print("Nenhum dado cadastrado.")
        return
    notas = [u['nota'] for u in dados]
    media = sum(notas) / len(notas)
    print(f"\n📊 Média das notas: {media:.2f}")

def verificar_duas_etapas(nome, senha):
    dados = carregar_dados()
    for u in dados:
        if u['nome'] == nome and u['senha'] == senha:
            codigo = str(random.randint(1000, 9999))
            print(f"Código de verificação (simulado): {codigo}")
            entrada = input("Digite o código de verificação: ")
            if entrada == codigo:
                print("✅ Login realizado com sucesso!")
                return True
            else:
                print("❌ Código incorreto.")
                return False
    print("❌ Usuário ou senha incorretos.")
    return False

def trocar_senha():
    print("\n--- Recuperação de Senha ---")
    nome = input("Nome: ")
    idade = int(input("Confirme sua idade: "))
    dados = carregar_dados()
    for u in dados:
        if u['nome'] == nome and u['idade'] == idade:
            nova = input("Digite a nova senha: ")
            if len(nova) < 6:
                print("⚠️ Senha muito curta.")
                return
            u['senha'] = nova
            salvar_dados(dados)
            print("🔐 Senha atualizada com sucesso.")
            return
    print("❌ Usuário não encontrado.")

def excluir_usuario():
    print("\n--- Exclusão de Usuário ---")
    nome = input("Digite o nome do usuário a ser excluído: ")
    dados = carregar_dados()
    novos_dados = [u for u in dados if u['nome'] != nome]
    if len(novos_dados) < len(dados):
        salvar_dados(novos_dados)
        print("🗑️ Usuário excluído.")
    else:
        print("Usuário não encontrado.")

def menu():
    while True:
        print("\n--- Plataforma Digital ONG ---")
        print("1. Cadastrar novo usuário")
        print("2. Mostrar usuários cadastrados")
        print("3. Calcular média das notas")
        print("4. Ver medidas LGPD")
        print("5. Login com verificação de duas etapas")
        print("6. Trocar senha")
        print("7. Excluir usuário")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_usuario()
        elif opcao == "2":
            mostrar_usuarios()
        elif opcao == "3":
            calcular_media()
        elif opcao == "4":
            exibir_medidas_lgpd()
        elif opcao == "5":
            nome = input("Nome: ")
            senha = input("Senha: ")
            verificar_duas_etapas(nome, senha)
        elif opcao == "6":
            trocar_senha()
        elif opcao == "7":
            excluir_usuario()
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
