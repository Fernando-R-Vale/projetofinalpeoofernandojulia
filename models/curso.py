import json
from models.model import Modelo
class curso:
  def __init__(self, id, nome, professores, vagas, nivel, id_departamento):
    self.__id = id
    self.__nome = nome
    self.__professores = professores
    self.__vagas = vagas
    self.__nivel = nivel
    self.__departamento = id_departamento
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_professores(self): return self.__professores
  def get_vagas(self): return self.__vagas
  def get_nivel(self): return self.__nivel
  def get_departamento(self): return self.__departamento

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_professores(self, professores): self.__professores = professores
  def set_vagas(self, vagas): self.__vagas = vagas
  def set_nivel(self, nivel): self.__nivel = nivel
  def set_departamento(self, departamento): self.__departamento = departamento

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__professores == x.__professores and self.__vagas == x.__vagas and self.__nivel == x.__nivel and x.__departamento == self.__departamento:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__professores} - {self.__vagas} - {self.__nivel} - {self.__departamento}"


class Ncurso(Modelo):

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("cursos.json", mode="r") as arquivo:
        cursos_json = json.load(arquivo)
        for obj in cursos_json:
          aux = curso(obj["_curso__id"], obj["_curso__nome"], obj["_curso__professores"], obj["_curso__vagas"], obj["_curso__nivel"], obj["_curso__departamento"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("cursos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)
