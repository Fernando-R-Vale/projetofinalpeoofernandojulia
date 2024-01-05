import json
from model import Modelo
class Universidade:
  def __init__(self, id, nome, local, telefone):
    self.__id = id
    self.__nome = nome
    self.__local = local
    self.__telefone = telefone

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_local(self): return self.__local
  def get_telefone(self): return self.__telefone

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_local(self, local): self.__local = local
  def set_telefone(self, telefone): self.__telefone = telefone

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__local == x.__local and self.__telefone == x.__telefone:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__local} - {self.__telefone}"

  def to_json(self):
    return {
      'id': self.__id,
      'nome': self.__nome,
      'local': self.__local,
      'telefone': self.__telefone}


class NUniversidades(Modelo):
  __universisdades = []

  @classmethod
  def abrir(cls):
    cls.__universisdades = []
    try:
      with open("universisdades.json", mode="r") as arquivo:
        universisdades_json = json.load(arquivo)
        for obj in universisdades_json:
          aux = Universidade(
            obj["id"],
            obj["nome"],
            obj["local"], obj["telefone"])
          cls.__universisdades.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("universisdades.json", mode="w") as arquivo:
      json.dump(cls.__universisdades, arquivo, default=Universidade.to_json)
