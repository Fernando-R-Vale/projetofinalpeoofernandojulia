import json
from models.model import Modelo
class adm:
  def __init__(self, id, email, senha):
    self.__id = id
    self.__email = email
    self.__senha = senha


  def get_id(self): return self.__id
  def get_email(self): return self.__email
  def get_senha(self): return self.__senha

  def set_id(self, id): self.__id = id
  def set_email(self, email): self.__email = email
  def set_senha(self, senha): self.__senha = senha

  def __eq__(self, x):
    if self.__id == x.__id and self.__email == x.__email and self.__senha == x.__senha:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__email} - {self.__senha}"


class Nadm(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("adms.json", mode="r") as arquivo:
        adms_json = json.load(arquivo)
        for obj in adms_json:
          aux = adm(obj["_adm__id"], obj["_adm__email"], obj["_adm__senha"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("adms.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)