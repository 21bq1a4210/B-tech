import React from 'react';

const TableView = () => {
  const data = [
    { ID: 1, Name: 'Santhosh', Age: 20 },
    { ID: 2, Name: 'Ramesh', Age: 21 },
    { ID: 3, Name: 'Ravi', Age: 20 },
    { ID: 4, Name: 'Swamy', Age: 21 },
    { ID: 5, Name: 'Nehru', Age: 21 },
  ];

  const renderTableHeader = () => Object.keys(data[0]).map((key) => <th key={key}>{key}</th>);

  const renderTableData = () =>
    data.map((item, index) => (
      <tr key={index} style={{ backgroundColor: index % 2 === 0 ? '#f2f2f2' : 'white' }}>
        {Object.values(item).map((value, index) => (
          <td key={index} style={{ border: '1px solid black', textAlign: 'center' }}>
            {value}
          </td>
        ))}
      </tr>
    ));

  const tableStyle = {
    borderCollapse: 'collapse',
    width: '70%',
    margin: '20px auto',
    border: '1px solid blue',
  };

  return (
    <div>
      <h1 style={{ textAlign: 'center', borderBottom: '2px solid blue', paddingTop: '20px', marginBottom: '100px' }}>
        Array of Objects - TableView
      </h1>
      <table style={tableStyle}>
        <thead style={{ backgroundColor: '#3498db' }}>
          <tr>{renderTableHeader()}</tr>
        </thead>
        <tbody>{renderTableData()}</tbody>
      </table>
    </div>
  );
};

export default TableView;