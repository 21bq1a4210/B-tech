import React, { useState, useEffect } from 'react';

function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setSeconds(seconds => seconds + 1);
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  useEffect(() => {
    document.title = `You've been on this page for ${seconds} seconds`;
  }, [seconds]);

  return (
    <div>
      <p>You've been on this page for {seconds} seconds</p>
    </div>
  );
}

export default Timer;
