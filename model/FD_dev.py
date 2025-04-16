import re
import sqlite3 as sql

class DBmanager:
  def __init__(self,DBpath):
    self.DB=sql.connect(DBpath)
    self.cur=self.DB.cursor()

  def id_from_phone(self,phone:int)->int:
    """finds ecosystem client id from mobile account phone"""
    self.cur.execute(f"""
            SELECT id FROM ecosystem_mapping
            JOIN mobile_clients ON mobile_user_id=client_id
            WHERE phone="{phone}"
            """)
    results=[e[0] for e in self.cur.fetchall()]
    if len(results)<1:
      raise Exception(f"This phone (+{phone}) is not registered")
    if len(results)>1:
      print(f"WARN: phone (+{phone}) is registered on multiple accounts, only one was returned")
    return results[0]

  def mobile_info(self,id:int)->tuple[int,str,str,str]:
    """
    Find mobile client data from ecosystem id
    :return: phone,clientId,fio,address
    """
    self.cur.execute(f"""
            SELECT phone,client_id,fio,address FROM mobile_clients
            JOIN ecosystem_mapping as eco ON client_id=mobile_user_id
            WHERE id='{id}'
            """)
    results=self.cur.fetchall()
    if len(results)<1:
      raise Exception(f"Client (id={id}) dont have mobile account")
    if len(results)>1:
      print(f"WARN: Client (id={id}) has multiple mobile accounts, only one was returned")
    return results[0]

  def phone_from_id(self,id:int)->int:
    """finds client phone from ecosystem client id"""
    return self.mobile_info(id)[0]

  def id_from_bank_user(self,bank_user:int)->int:
    """finds ecosystem client id from bank account id"""
    self.cur.execute(f"""
            SELECT id FROM ecosystem_mapping  
            JOIN bank_clients ON bank_id=userId
            WHERE userId='{bank_user}'
            """)
    results=[e[0] for e in self.cur.fetchall()]
    if len(results)<1:
      raise Exception(f"Bank user №{bank_user} is not connected to ecosystem")
    if len(results)>1:
      print(f"WARN: Bank user №{bank_user} is registered on multiple accounts, only one was returned")
    return results[0]

  def bank_client(self,id:int)->tuple[str,int,int,str]:
    """finds bank client info from ecosystem client id
    :returns: userId, bank_account, phone, FIO"""
    self.cur.execute(f"""
            SELECT userId,accout,phone,fio FROM bank_clients
            JOIN ecosystem_mapping ON userId=bank_id
            WHERE id='{id}'
            """)
    results = self.cur.fetchall()
    if len(results)<1:
      raise Exception(f"Client (id={id}) dont have bank account")
    if len(results)>1:
      print(f"WARN: Client (id={id}) has multiple bank accounts, only one was returned")
    return results[0]

  def bank_account(self,id:int)->int:
    """returns bank account for ecosystem client id"""
    return self.bank_client(id)[1]

  def id_from_bank_account(self,bank_account:int)->int:
    """Finds ecosystem client id from bank account id"""
    self.cur.execute(f"""
            SELECT id FROM ecosystem_mapping  
            JOIN bank_clients ON bank_id=userId
            WHERE accout='{bank_account}'
            """)
    results=[e[0] for e in self.cur.fetchall()]
    if len(results)<1:
      raise Exception(f"Bank account №{bank_account} is not connected to ecosystem")
    if len(results)>1:
      print(f"WARN: Bank account №{bank_account} is registered on multiple accounts, only one was returned")
    return results[0]

  def find_calls(self,phone,incoming=True,outgoing=False)->list[tuple[int,int]]:
    """
    finds phone calls from or to specific phone number

    :param phone: phone number
    :param incoming: return calls to this phone
    :param outgoing: return call from this phone
    :return: [(calling_phone,called_phone,call_date,call_duration),...]
    """
    self.cur.execute(f"""
            SELECT from_call,to_call,event_date,duration_sec FROM mobile_build
            WHERE to_call="{phone if incoming else 0}"
             or from_call="{phone if outgoing else 0}"
            """)
    results = self.cur.fetchall()
    return results

  def fetch_call(self,from_call:int,to_call:int):
    """find all calls from <from_call> to <to_call>
    :returns: [(calling_phone,called_phone,call_date,call_duration),...] """
    self.cur.execute(f"""
            SELECT from_call,to_call,event_date,duration_sec FROM mobile_build
            WHERE to_call="{to_call}"
             and from_call="{from_call}"
            """)
    results=self.cur.fetchall()
    return results

  def find_transactions(self,account,incoming:bool=False,outgoing:bool=True,value:float=None,value_type:str="equal"):
    """
    Find all transactions from or to an account
    :param account: bank account id
    :param incoming: return incoming transactions
    :param outgoing: return outgoing transactions
    :param value: *optional, filter by value
    :param value_type: filter type ("equal" or "more")
    :return: [(sender,receiver,value,date),...]
    """
    match value_type:
      case "equal":sign="="
      case "more":sign=">"
      case _:raise AttributeError(f"incorrect value filter type {repr(value_type)}")

    self.cur.execute(f"""
            SELECT account_out,account_in,value,event_date from bank_transactions
            WHERE (account_in="{account if incoming else 0}"
            OR account_out="{account if outgoing else 0}")
            {f"AND value{sign}'{value}'" if value is not None else ""}
            """)
    results = self.cur.fetchall()
    return results

  def delivery_info(self,id)->list[tuple[str,str,int,str,str]]:
    """finds marketplace deliveries info from ecosystem client id
    :returns: [(userId, FIO, phone, address, date),...]"""
    self.cur.execute(f"""
            SELECT user_id,contact_fio,contact_phone,address,event_date FROM market_place_delivery
            JOIN ecosystem_mapping ON user_id=market_plece_user_id
            WHERE id='{id}'
            """)
    results = self.cur.fetchall()
    return results

def fraud_search(db:DBmanager):
  cur = db.cur

  # Берём столбцы id клиента и текст обращения
  cur.execute("SELECT uerId,text from bank_complaints;")

  # Обрабатываем данные
  for bank_user, text in cur.fetchall():
    # Пишем id клиента и текст обращения
    print(bank_user, text)

    # Берём из текста обращения сумму
    value = re.findall(r"(-?\d+)р", text)[0]

    # Ищем и выводим клиента по id в экосистеме
    user = db.id_from_bank_user(bank_user)
    print("ecosystem client id =", user)

    user_account=db.bank_account(user)
    fraud_bank = db.find_transactions(user_account,value=value)
    print("fraud account:", fraud_bank[0][0])

    # Ищем и выводим номер телефона клиента
    phone = db.phone_from_id(user)
    print("client phone:", phone)

    # Ищем и выводим номер телефона мошенника
    fraud_phone = db.find_calls(phone)[0][0]
    print("fraud phone:", fraud_phone)

    # Ищем и выводим id мошенника в экосистеме
    fraud_id=db.id_from_phone(fraud_phone)
    print("ecosystem fraud id", fraud_id)

    # Ищем и выводим адрес и ФИО мошенника
    _,fraud_fio,_,fraud_address,_=db.delivery_info(fraud_id)[0]
    print("fraud address:", fraud_address)
    print("fraud fio:", fraud_fio)

def fraud_detection(db):
  ...

if __name__=="__main__":
  #создаём менеджер базы данных
  db=DBmanager("bank.db")
  #ищем мошенника
  fraud_search(db)
  fraud_detection(db)