from models.adm import adm, Nadm
from models.departamento import departamento, Ndepartamento
from models.universisdade import Universidade, NUniversidades
from models.curso import curso, Ncurso
class View:
  def Adm_inserir(email, senha):
    a = int(0)
    x = adm(a, email, senha)
    Nadm.inserir(x)

  def Adm_listar():
    return Nadm.listar()
  
  def Adm_listar_id(id):
    return Nadm.listar_id(id)

  def Adm_atualizar(id, email, senha):
    x = adm(id, email, senha)
    Nadm.atualizar(x)
    
  def Adm_excluir(id):
    x = adm(id, "", "")
    Nadm.excluir(x)  
  
  def Adm():
    for x in View.Adm_listar():
      if x.get_email() == "admin": return
    View.Adm_inserir("admin", "admin")  
 
  def adm_login(email, senha):
    for x in View.Adm_listar():
      if x.get_email() == email and x.get_senha() == senha:
        return x
    return None

  def departamento_listar():
    return Ndepartamento.listar()

  def departamento_listar_id(id):
    return Ndepartamento.listar_id(id)

  def departamento_inserir(nome, id_universidade, telefone):
    Ndepartamento.inserir(departamento(0, nome, id_universidade, telefone))

  def departamento_atualizar(id, nome, id_universidade, telefone):
    Ndepartamento.atualizar(departamento(id, nome, id_universidade, telefone))

  def departamento_excluir(id):
    Ndepartamento.excluir(departamento(id, "", 0, ""))

  def universidade_listar_id(id):
    return NUniversidades.listar_id(id)
  
  def universidade_listar():
    return NUniversidades.listar()

  def universidade_inserir(nome, local, telefone):
    NUniversidades.inserir(Universidade(0, nome, local, telefone))

  def universidade_atualizar(id, nome, local, telefone):
    NUniversidades.atualizar(Universidade(id, nome, local, telefone))

  def universidade_excluir(id):
    NUniversidades.excluir(Universidade(id, "", "", ""))

  def curso_listar():
    return Ncurso.listar()

  def curso_inserir(nome, professores, vagas, nivel, id_departamento):
    Ncurso.inserir(curso(0, nome, professores, vagas, nivel, id_departamento))

  def curso_atualizar(id, nome, professores, vagas, nivel, id_departamento):
    Ncurso.atualizar(curso(id, nome, professores, vagas, nivel, id_departamento))

  def curso_excluir(id):
    Ncurso.excluir(curso(id, "", "", "", "",""))
