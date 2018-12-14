from storage import *


class PersonInfo(DataStorage):
    def field(self):
        self.name = Column(String(50), comment='姓名')
        self.age = Column(String(50), comment='年龄')
        self.address = Column(String(50), comment='地址')


class SchoolInfo(DataStorage):
    def field(self):
        self.school = Column(String(50), comment='学校')
        self.name = Column(String(50), comment='姓名')

if __name__=='__main__':
    DATABASE_CONNECTION = 'mysql+pymysql://root:1234@localhost/spiderdb?charset=utf8mb4'
    person = PersonInfo(DATABASE_CONNECTION)
    school = SchoolInfo(DATABASE_CONNECTION)
    # Insert multiple data to personInfo
    personInfo = [{'name': 'Lucy', 'age': '21', 'address': '北京市'},
                  {'name': 'Lily', 'age': '18', 'address': '上海市'}]
    person.insert(personInfo)
    # Insert single data to schoolInfo
    schoolInfo = {'name': 'Lucy', 'school': '清华大学'}
    school.insert(schoolInfo)

    # Update data to personInfo with condition
    condition = {'id': 1}
    personInfo = {'name': 'Lucy', 'age': '22', 'address': '广州市'}
    person.update(personInfo, condition)
    # Update data to schoolInfo
    schoolInfo = {'name': 'Lucy', 'school': '北京大学'}
    school.update(schoolInfo, condition)
