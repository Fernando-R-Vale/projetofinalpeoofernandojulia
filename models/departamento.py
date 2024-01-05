import json
from models.model import Modelo
class departamento:
  def __init__(self, id, nome, id_universidade, telefone):
    self.__id = id
    self.__nome = nome
    self.__id_universidade = id_universidade
    self.__telefone = telefone

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_id_universidade(self): return self.__id_universidade
  def get_telefone(self): return self.__telefone

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_id_universidade(self, id_universidade): self.__id_universidade = id_universidade
  def set_telefone(self, telefone): self.__telefone = telefone

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__id_universidade == x.__id_universidade and self.__telefone == x.__telefone:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__id_universidade} - {self.__telefone}"


class Ndepartamento(Modelo):
  departamentos = []


  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("departamentos.json", mode="r") as arquivo:
        departamentos_json = json.load(arquivo)
        for obj in departamentos_json:
          aux = departamento(obj["_departamento__id"], obj["_departamento__nome"], obj["_departamento__id_universidade"], obj["_departamento__telefone"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("departamentos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)
