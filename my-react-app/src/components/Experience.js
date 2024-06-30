// src/components/Experience.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Experience.css'; // Import CSS for styling

const Experience = () => {
    const [experiences, setExperiences] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/experiences')
            .then(response => {
                setExperiences(response.data);
            })
            .catch(error => {
                console.error('Error fetching experience data:', error);
            });
    }, []);

    return (
        <div className="experience-container">
            <h2>Experience</h2>
            <table className="experience-table">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Company</th>
                        <th>Start Date</th>
                        <th>End Date</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    {experiences.map(experience => (
                        <tr key={experience.id}>
                            <td>{experience.title}</td>
                            <td>{experience.company}</td>
                            <td>{experience.start_date}</td>
                            <td>{experience.end_date}</td>
                            <td>{experience.description}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Experience;
