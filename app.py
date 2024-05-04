from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# defining a class called persons where our required details are mentioned and their types
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Person {self.id}: {self.name}>"
        
@app.route('/persons', methods=['POST'])
def create_person():
    data = request.json
    new_person = Person(name=data['name'], mobile=data['mobile'], email=data['email'], country=data['country'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully!'}), 201

@app.route('/persons', methods=['GET'])
def get_all_persons():
    persons = Person.query.all()
    output = [{'id': person.id, 'name': person.name, 'mobile': person.mobile, 'email': person.email, 'country': person.country} for person in persons]
    return jsonify({'persons': output})

@app.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get_or_404(person_id)
    return jsonify({'id': person.id, 'name': person.name, 'mobile': person.mobile, 'email': person.email, 'country': person.country})

@app.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = Person.query.get_or_404(person_id)
    data = request.json
    person.name = data['name']
    person.mobile = data['mobile']
    person.email = data['email']
    person.country = data['country']
    db.session.commit()
    return jsonify({'message': 'Person updated successfully!'})

@app.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
