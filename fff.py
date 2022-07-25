#Backend Application
#Class and method name/s
#API to CRUD aircraft, engines, hangars and workers.

class air_CRUD (object):
    def __init__(self, conn):
        self.conn = conn
    def insert_AIRCRAFT(def, engine_id):
    
        dml=f"INSERT into AIRCAFT VALUES(0, {engine_id}, 30, 2)"
        
#Frontend Application
#Class/Component/Page name/s
#Uses backend application API to build User Interface (UI)



if __name__ == "__main__":
    conn = Connect_to_db()
    air=air_CRUD(conn)
    engine_id= air_CRUD.get_engine_id(engine_name='TEST_ENGINE')
    air.insert_AIRCRAFT(engine_id)