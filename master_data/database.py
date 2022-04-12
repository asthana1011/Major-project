import sqlite3 as sq

class q_controls:
    def __init__(self):
        self.queue = sq.connect("music_queue.db")
        self.pointer = self.queue.cursor()
    
    def create_new_queue(self, q_name):
        command = '''create table if not exists '''+q_name+''' (serial INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT(100))'''
        self.pointer.execute(command)
        self.queue.commit()

    def remove_queue(self, q_name):
        self.pointer.execute("DROP TABLE "+ q_name)
        self.queue.commit()

    def update_queue(self, q_name, file_name):
        a = "'"
        file_name =a+file_name+a 
        command = "INSERT INTO {}(filename) VALUES({})".format(q_name, file_name)
        self.pointer.execute(command)
        self.queue.commit()

    def show_queue(self):
        queue_list = []
        self.pointer.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for i in self.pointer.fetchall()[1:]:
            queue_list.append(i[0])
        return queue_list

    def show_contents(self, q_name):
        rec = []
        self.pointer.execute("select * from {}".format(q_name))
        while(True):
            record = self.pointer.fetchone()
            if record == None:
                break
            rec.append(record[1])
        return rec

    def drop_queue(self, q_name):
        command = "DROP TABLE "+q_name
        self.pointer.execute(command)
        self.queue.commit()
        
        


#w = q_controls()
#w.drop_queue()
#print(w.show_queue())
