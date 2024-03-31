import React, { useState } from 'react';

const BMICalculator = () => {
  const [height, setHeight] = useState('');
  const [weight, setWeight] = useState('');
  const [bmi, setBMI] = useState(null);

  const calculateBMI = () => {
    const bmiValue = height && weight ? (weight / ((height / 100) ** 2)).toFixed(2) : null;
    setBMI(bmiValue);
  };

  return (
    <div>
      <h2>BMI Calculator</h2>
      <div>
        <label htmlFor="height">Height (in cm):</label>
        <input
          type="number"
          id="height"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="weight">Weight (in kg):</label>
        <input
          type="number"
          id="weight"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
        />
      </div>
      <button onClick={calculateBMI}>Calculate BMI</button>
      {bmi && (
        <div>
          <h3>Your BMI:</h3>
          <p>{bmi}</p>
        </div>
      )}
    </div>
  );
};

export default BMICalculator;
