from __init__ import db

class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=True, unique=True)

    # Create a static method to create the table 'departments'
    def create(self):
        db.session.add(self)
        db.session.commit()

    # Create a class method that can modify the class DepartmentModel
    @classmethod
    def check_department_exists(cls, department_name):
        record = cls.query.filter_by(name=department_name).first()
        if record:
            return True
        else:
            return False
    
    # A class method to fetch all departments
    @classmethod
    def fetch_all_departments(cls):
        return cls.query.all()

    # A class method to fetch departments by id
    @classmethod
    def fetch_department_by_id(cls, id):
        return cls.query.filter_by(id=id).first()