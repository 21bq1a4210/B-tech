import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timerId = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(timerId);
  }, []);

  return (
    <div>
      <h1 style={{ textAlign: 'center', borderBottom: '2px solid orange', paddingTop: '20px', color: 'blue' }}>Analog - Digital Clock</h1>
      <div className='clock-container'>
        <div className="digital-clock">
          <h2>
            {time.getHours().toString().padStart(2, "0")}:
            {time.getMinutes().toString().padStart(2, "0")}:
            {time.getSeconds().toString().padStart(2, "0")}
            <sup style={{ fontSize: '0.4em', verticalAlign: 'top' }}>{time.getHours() >= 12 ? 'PM' : 'AM'}</sup>
          </h2>
          <div className="date-container" style={{ textAlign: 'center' }}>
            <p style={{ fontSize: '0.6em', margin: '0' }}>{new Intl.DateTimeFormat('en-US', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' }).format(time)}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
