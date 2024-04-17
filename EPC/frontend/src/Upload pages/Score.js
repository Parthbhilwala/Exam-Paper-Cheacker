import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import './Score.css';

const Score = () => {
    const location = useLocation();
    const data = location.state.data; // Access the passed data
    const navigate = useNavigate();

    const handleGoBack = () => {
        navigate(-1); // Go back to the previous page
    };

    // Calculate the result and total score
    const result = data.result;
    const total = data.total;

    return (
        <div className="score">
            <h1>Your final score is:</h1>
            <div className="circle">
                {result}/{total}
            </div>
            <button className="blue-button" onClick={handleGoBack}>Back</button>
        </div>
    );
};

export default Score;
