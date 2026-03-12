from database.conexao import conectar
def recuperar_requisitos():
    conexao, cursor = conectar()
    cursor.execute ("""
                SELECT cod_requisito, descricao, nivel, valor, situacao FROM tb_requisitos;
                    """)
    requisitos = cursor.fetchall()
    conexao.close()
    return requisitos