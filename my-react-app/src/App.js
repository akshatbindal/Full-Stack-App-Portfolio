// src/App.js

import React from 'react';
import Education from './components/Education';
import Experience from './components/Experience';
import Projects from './components/Projects';
import Skills from './components/Skills';
import Certifications from './components/Certifications';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>My Portfolio</h1>
            </header>
            <main className="App-content">
                <Education />
                <Experience />
                <Projects />
                <Skills />
                <Certifications />
            </main>
        </div>
    );
}

export default App;
