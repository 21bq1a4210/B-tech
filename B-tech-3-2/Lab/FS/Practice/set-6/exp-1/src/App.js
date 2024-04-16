import React from 'react';
const TableView = ({ data }) => (
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Age</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      {data.map((item, index) => (
        <tr key={index}>
          <td>{item.name}</td>
          <td>{item.age}</td>
          <td>{item.email}</td>
        </tr>
      ))}
    </tbody>
  </table>
);

const App = () => {
  const data = [
    { name: 'John', age: 25, email: 'john@example.com' },
    { name: 'Alice', age: 30, email: 'alice@example.com' },
    { name: 'Bob', age: 35, email: 'bob@example.com' }
  ];

  return (
    <div style={{textAlign: 'center'}}>
      <h1>Table View Example</h1>
      <TableView data={data} />
    </div>
  );
};

export default App;
