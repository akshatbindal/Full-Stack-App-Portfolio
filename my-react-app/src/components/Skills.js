// src/components/Skills.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Skills.css'; // Import CSS for styling

const Skills = () => {
    const [skills, setSkills] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/skills')
            .then(response => {
                setSkills(response.data);
            })
            .catch(error => {
                console.error('Error fetching skills data:', error);
            });
    }, []);

    return (
        <div className="skills-container">
            <h2>Skills</h2>
            <table className="skills-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Level</th>
                    </tr>
                </thead>
                <tbody>
                    {skills.map(skill => (
                        <tr key={skill.id}>
                            <td>{skill.name}</td>
                            <td>{skill.level}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Skills;
