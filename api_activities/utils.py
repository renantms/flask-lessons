from models import People

def insert_people():
    person = People(name='Renan', age=19)
    print(person)
    person.save()

def query_people():
    people = People.query.all()
    print(people)
   # person = People.query.filter_by(name='Renan')
   # for p in person:
   #     print(p)

def alter_person():
    person = People.query.filter_by(name='Renan').first()
    person.age = 21
    person.save()

def delete_person():
    person = People.query.filter_by(name='Renan').first()
    person.delete()

if __name__ == "__main__":
    # insert()
    #alter_people()
    delete_person()
    query_people()