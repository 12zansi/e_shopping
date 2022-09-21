from back_end.Models.bank_account import BankAccount
from back_end.database.session import start_session
from fastapi import Depends
from requests import Session
from sqlalchemy import and_
from back_end.database.tables.tb_bank_account import TBBankAccounts
from back_end.dependencies.login import UserLogin, token_auth_scheme

class UserBankAccount(UserLogin):
     
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db  

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data 

    def add_bank_account(self, bank: BankAccount, token: str = Depends(token_auth_scheme)):
        user = UserBankAccount._get_user(token)
  
        query = self.db.query(TBBankAccounts).filter(TBBankAccounts.user_id == user[1]).first()

        if query:

            return { "message": "you are already have account"}

        account = TBBankAccounts(
               holder_name = bank.holder_name,
               account_no = bank.account_no,
               branch_name = bank.branch_name,
               ifsc_code = bank.ifsc_code,
               user_id = user[1]
              )

        UserBankAccount._add_in_table(self, account)

        return account


    def view_bank_account(self, id: int, token: str = Depends(token_auth_scheme)):
        user = UserBankAccount._get_user(token)

        query = self.db.query(TBBankAccounts).filter(and_(TBBankAccounts.id == id, TBBankAccounts.user_id == user[1])).all()

        return { "data":query , "success": True}

    def change_bank_account(self, id: int, bank: BankAccount, token: str = Depends(token_auth_scheme)):
        user = UserBankAccount._get_user(token)

        query = self.db.query(TBBankAccounts).filter(TBBankAccounts.id == id, TBBankAccounts.user_id == user[1])\
            .update({ 
               TBBankAccounts.holder_name: bank.holder_name,
               TBBankAccounts.account_no: bank.account_no,
               TBBankAccounts.branch_name: bank.branch_name,
               TBBankAccounts.ifsc_code: bank.ifsc_code,
               TBBankAccounts.user_id: user[1] })

        if query:
            self.db.commit()
            return { "message": "account updated"}

        return { "message": "account doesn't exist"}