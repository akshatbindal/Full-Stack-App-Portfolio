from flask import Flask, jsonify, request
from src.models import db, Education, Experience, Projects, Skills, Certifications
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Define RESTful API endpoints

# Education endpoints
@app.route('/educations', methods=['GET'])
def get_educations():
    educations = Education.query.all()
    return jsonify([education.to_dict() for education in educations])

@app.route('/education', methods=['POST'])
def add_education():
    data = request.json
    new_education = Education(
        degree=data['degree'],
        institution=data['institution'],
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        grade=data.get('grade')
    )
    db.session.add(new_education)
    db.session.commit()
    return jsonify(new_education.to_dict()), 201

# Similarly define other endpoints for Experience, Projects, Skills, and Certifications
# ...

# Add to_dict methods to your models for serialization
def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Education.to_dict = to_dict
Experience.to_dict = to_dict
Projects.to_dict = to_dict
Skills.to_dict = to_dict
Certifications.to_dict = to_dict

if __name__ == '__main__':
    app.run(debug=True)
