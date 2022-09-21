from fastapi import Depends
from requests import Session
from back_end.database.session import start_session
from back_end.database.tables.tb_category import TBCategories
from sqlalchemy.orm import aliased


class UserCategory:
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def get_category(self, id: int):
        query  = self.db.query(TBCategories).filter(TBCategories.id == id).first()

        return {"data": query,"success":True}

    def get_child_category(self, id: int): 
      
      beginning_getter = self.db.query(TBCategories).filter(TBCategories.parent_id ==  id).cte(name='parent_for', recursive=True)
      with_recursive = beginning_getter.union_all(self.db.query(TBCategories).filter(TBCategories.parent_id == beginning_getter.c.id))
      result = self.db.query(with_recursive).all()
     
      name_node = {}
      root =  {'name': 'Root', 'children': []}
      for i in result:
          parent_node = name_node.get(i[3])
         
          # print(parent_node)
          if not parent_node:
            name_node[i[3]] = parent_node = {}
        
            root['children'].append(parent_node)
            # print(root)
           
          name_node[i[0]] = child_node = {'name': i[1]}
          print(name_node[i[0]])
          parent_node.setdefault('child',[]).append(child_node)
          print(parent_node)
      
      childs = root['children'][0]['child']

      return {"data":childs, "success": True}

