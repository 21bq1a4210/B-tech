import React, { useState } from 'react';

function ColorChanger() {
  const [textColor, setTextColor] = useState('black');

  const handleColorChange = (event) => {
    setTextColor(event.target.value);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <div style={{
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        zIndex: '-1',
        opacity: '0.3',
        fontFamily: 'Arial sans-serif',
        fontSize: 'Normal',
        color: 'blue',
      }}>Shesank</div>
      <label htmlFor='colorpicker'>Select Text Color:</label>
      <input
        type='color'
        id='colorpicker'
        value={textColor}
        onChange={handleColorChange}
      />
      <div style={{
        color: textColor,
        marginTop: '20px',
        fontFamily: 'Arial, sans-serif',
        fontSize: '20px',
        fontStyle: 'normal',
        textDecoration: 'none'
      }}>
        <h1>It's your choice, see the Magic!</h1>
      </div>

    </div>
  );
}

export default ColorChanger;
