from models.TaskModel import db, Task

class TaskService:
    @staticmethod
    def create_task(user_id, description):
        task = Task(descripcion=description, user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_all_tasks():
        return Task.query.all()     
    
    @staticmethod
    def mark_task_as_done(task_id):
        task = Task.query.get(task_id)
        if task:
            task.estado = 'terminada'
            db.session.commit()
            return task
        return None
    
    @staticmethod
    def get_tasks_done():
        #all_tasks = Task.query.filter_by(estado = "terminada").all()
        all_tasks = db.session.query(Task).filter_by(estado = "terminada").all()
        print(all_tasks)
        #return list(map(lambda x: x.serialize(), all_tasks))
        return all_tasks