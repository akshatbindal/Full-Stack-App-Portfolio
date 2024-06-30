// src/components/Certifications.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Certifications.css'; // Import CSS for styling

const Certifications = () => {
    const [certifications, setCertifications] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/certifications')
            .then(response => {
                setCertifications(response.data);
            })
            .catch(error => {
                console.error('Error fetching certifications data:', error);
            });
    }, []);

    return (
        <div className="certifications-container">
            <h2>Certifications</h2>
            <table className="certifications-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Authority</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {certifications.map(certification => (
                        <tr key={certification.id}>
                            <td>{certification.name}</td>
                            <td>{certification.authority}</td>
                            <td>{certification.date}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Certifications;
