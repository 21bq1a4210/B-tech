import React, { createContext, useContext } from 'react';

const ThemeContext = createContext('dark');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  );
}

function Toolbar() {
  const theme = useContext(ThemeContext);
  return (
    <div>
      <p>Current theme: {theme}</p>
    </div>
  );
}

export default App;
