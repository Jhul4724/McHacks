import logo from './logo.svg';
import './App.css';
import React from 'react';
import Navbar from './Navbar';
import { useState, useEffect } from 'react';

function App() {

  const [message, setMessage] = useState('bye')

  useEffect(() => {
    fetch("http://localhost:5000/")
    .then(res => setMessage(res.text()))
  }, [])
  
  return (
    <div className="App">
          <Navbar ></Navbar>
          <form action="{{ url_for('info')}}" method="post">
        <label for="firstname">First Name:</label>
        <input type="text" id="first name" name="fname" placeholder="first name" />
        <label for="lastname">Last Name:</label>
        <input type="text" id="last name" name="lname" placeholder="last name" />
        <button type="submit">Login</button></form>
    </div>
  );
}

export default App;
