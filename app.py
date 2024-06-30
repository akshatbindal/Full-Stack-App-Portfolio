from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from src.models import db, Education, Experience, Projects, Skills, Certifications

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Routes for Education
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

@app.route('/education/<int:id>', methods=['PUT'])
def update_education(id):
    data = request.json
    education = Education.query.get_or_404(id)
    education.degree = data['degree']
    education.institution = data['institution']
    education.start_date = data['start_date']
    education.end_date = data.get('end_date')
    education.grade = data.get('grade')
    db.session.commit()
    return jsonify(education.to_dict())

@app.route('/education/<int:id>', methods=['DELETE'])
def delete_education(id):
    education = Education.query.get_or_404(id)
    db.session.delete(education)
    db.session.commit()
    return '', 204

# Routes for Experience

@app.route('/experiences', methods=['GET'])
def get_experiences():
    experiences = Experience.query.all()
    return jsonify([experience.to_dict() for experience in experiences])

@app.route('/experience', methods=['POST'])
def add_experience():
    data = request.json
    new_experience = Experience(
        title=data['title'],
        company=data['company'],
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        description=data.get('description')
    )
    db.session.add(new_experience)
    db.session.commit()
    return jsonify(new_experience.to_dict()), 201

@app.route('/experience/<int:id>', methods=['PUT'])
def update_experience(id):
    data = request.json
    experience = Experience.query.get_or_404(id)
    experience.title = data['title']
    experience.company = data['company']
    experience.start_date = data['start_date']
    experience.end_date = data.get('end_date')
    experience.description = data.get('description')
    db.session.commit()
    return jsonify(experience.to_dict())

@app.route('/experience/<int:id>', methods=['DELETE'])
def delete_experience(id):
    experience = Experience.query.get_or_404(id)
    db.session.delete(experience)
    db.session.commit()
    return '', 204

# Routes for Projects

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Projects.query.all()
    return jsonify([project.to_dict() for project in projects])

@app.route('/project', methods=['POST'])
def add_project():
    data = request.json
    new_project = Projects(
        name=data['name'],
        description=data['description'],
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        link=data.get('link')
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.to_dict()), 201

@app.route('/project/<int:id>', methods=['PUT'])
def update_project(id):
    data = request.json
    project = Projects.query.get_or_404(id)
    project.name = data['name']
    project.description = data['description']
    project.start_date = data['start_date']
    project.end_date = data.get('end_date')
    project.link = data.get('link')
    db.session.commit()
    return jsonify(project.to_dict())

@app.route('/project/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Projects.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return '', 204

# Routes for Skills

@app.route('/skills', methods=['GET'])
def get_skills():
    skills = Skills.query.all()
    return jsonify([skill.to_dict() for skill in skills])

@app.route('/skill', methods=['POST'])
def add_skill():
    data = request.json
    new_skill = Skills(
        name=data['name'],
        level=data.get('level')
    )
    db.session.add(new_skill)
    db.session.commit()
    return jsonify(new_skill.to_dict()), 201

@app.route('/skill/<int:id>', methods=['PUT'])
def update_skill(id):
    data = request.json
    skill = Skills.query.get_or_404(id)
    skill.name = data['name']
    skill.level = data.get('level')
    db.session.commit()
    return jsonify(skill.to_dict())

@app.route('/skill/<int:id>', methods=['DELETE'])
def delete_skill(id):
    skill = Skills.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    return '', 204

# Routes for Certifications

@app.route('/certifications', methods=['GET'])
def get_certifications():
    certifications = Certifications.query.all()
    return jsonify([certification.to_dict() for certification in certifications])

@app.route('/certification', methods=['POST'])
def add_certification():
    data = request.json
    new_certification = Certifications(
        name=data['name'],
        institution=data['institution'],
        date_awarded=data['date_awarded']
    )
    db.session.add(new_certification)
    db.session.commit()
    return jsonify(new_certification.to_dict()), 201

@app.route('/certification/<int:id>', methods=['PUT'])
def update_certification(id):
    data = request.json
    certification = Certifications.query.get_or_404(id)
    certification.name = data['name']
    certification.institution = data['institution']
    certification.date_awarded = data['date_awarded']
    db.session.commit()
    return jsonify(certification.to_dict())

@app.route('/certification/<int:id>', methods=['DELETE'])
def delete_certification(id):
    certification = Certifications.query.get_or_404(id)
    db.session.delete(certification)
    db.session.commit()
    return '', 204

def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Education.to_dict = to_dict
Experience.to_dict = to_dict
Projects.to_dict = to_dict
Skills.to_dict = to_dict
Certifications.to_dict = to_dict

if __name__ == '__main__':
    app.run(debug=True)
