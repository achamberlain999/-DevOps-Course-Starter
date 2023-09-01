import pymongo

class MongoDBClient:
    def __init__(self, database_connection_string, environment):
        self.DATABASE_CONNECTION_STRING = database_connection_string
        self.DATABASE_NAME = f"{environment}-tasko-database"
        self.TASK_COLLECTION_NAME = 'tasks'

        self.client = pymongo.MongoClient(self.DATABASE_CONNECTION_STRING)
        self.database = self.client[self.DATABASE_NAME]
        self.tasks = self.database[self.TASK_COLLECTION_NAME]
    
    def get_all_tasks(self):
        return self.tasks.find()

    def add_item_to_list(self, title, description):
        payload = {
            'name': title,
            'desc': description,
            'list': 'To do'
        }
        self.tasks.insert_one(payload)

    def complete_card(self, id):
        payload = {
            'list': 'Done'
        }
        self.tasks.update_one({ "_id": id }, { "$set": payload })

    def uncomplete_card(self, id):
        payload = {
            'list': 'To do'
        }
        self.tasks.update_one({ "_id": id }, { "$set": payload })

    def delete_card(self, id):
        self.tasks.delete_one({ "_id": id })
