import React, { useState, useEffect } from 'react';

const DigitalClock = () => {
  const [time, setTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const intervalID = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);

    return () => clearInterval(intervalID);
  }, []);

  return (
    <div>
      <h1>Digital Clock</h1>
      <p>Current Time: {time}</p>
    </div>
  );
};

const App = () => {
  return (
    <div>
      <DigitalClock />
    </div>
  );
};

export default App;