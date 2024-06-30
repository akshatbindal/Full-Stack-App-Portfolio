// src/components/Education.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Education.css'; // Import CSS for styling

const Education = () => {
    const [educations, setEducations] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/educations')
            .then(response => {
                setEducations(response.data);
            })
            .catch(error => {
                console.error('Error fetching education data:', error);
            });
    }, []);

    return (
        <div className="education-container">
            <h2>Education</h2>
            <table className="education-table">
                <thead>
                    <tr>
                        <th>Degree</th>
                        <th>Institution</th>
                        <th>Start Date</th>
                        <th>End Date</th>
                        <th>Grade</th>
                    </tr>
                </thead>
                <tbody>
                    {educations.map(education => (
                        <tr key={education.id}>
                            <td>{education.degree}</td>
                            <td>{education.institution}</td>
                            <td>{education.start_date}</td>
                            <td>{education.end_date}</td>
                            <td>{education.grade}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Education;
