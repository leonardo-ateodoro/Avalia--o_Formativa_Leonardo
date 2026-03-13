from database.conexao import conectar
def recuperar_requisitos():
    conexao, cursor = conectar()
    cursor.execute ("""
                SELECT cod_requisito, descricao, nivel, valor, situacao FROM tb_requisitos;
                    """)
    requisitos = cursor.fetchall()
    conexao.close()
    return requisitos

def excluir_requisitos(codigo):
    conexao, cursor = conectar()
    cursor.execute("""
                    DELETE FROM tb_requisitos WHERE cod_requisito = %s;
                    """, [codigo])
    conexao.commit()
    conexao.close()

def inserir_requisitos(descricao, nivel, valor, situacao= "Pendente"):
    conexao, cursor = conectar()
    cursor.execute("""
                   INSERT INTO tb_requisitos (descricao, nivel, valor, situacao)
                   VALUES (%s, %s, %s, %s);
                   """,
                [descricao, nivel, valor, situacao])
    conexao.commit()
    conexao.close()