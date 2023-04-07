from Bot.database import Mongo

def new_variable(user_id,name,value):
    return dict(
        user_id=user_id,
        name=name,
        value=value
    )


class DBVariables(Mongo):
    def __init__(self):
        self.col = self.db.variables

    def add_or_update_variable(self,user_id,name,value):
        if self.is_variable_exist(user_id,name):
            self.update_variable(user_id,name,value)
        else:
            self.add_variable(user_id,name,value)

    def add_variable(self,user_id,name,value):
        variable = new_variable(user_id,name,value)
        self.col.insert_one(variable)

    def update_variable(self,user_id,name,value):
        self.col.update_one({'user_id': user_id, 'name': name},{'$set':{'value':value}})

    def is_variable_exist(self,user_id,name):
        variable = self.col.find_one({'user_id': user_id, 'name': name})
        return True if variable else False

    def get_variable(self,user_id,name):
        if self.is_variable_exist(user_id,name):
            return self.col.find_one({'user_id': user_id, 'name': name})['value']
        return None

    def get_all_variables(self):
        return self.col.find()

db_variables = DBVariables()