import React, { useState } from 'react';
import './App.css';

const HotelBillScreen = () => {
  const [selectedItem, setSelectedItem] = useState(null);
  const [itemQuantity, setItemQuantity] = useState(1);
  const [transactions, setTransactions] = useState([]);
  const [currentDateTime, setCurrentDateTime] = useState(new Date());

  const items = [
    { id: 1, name: 'Idly', cost: 10 },
    { id: 2, name: 'Dosa', cost: 20 },
    { id: 3, name: 'Vada', cost: 20 },
    { id: 4, name: 'Poori', cost: 20 },
    { id: 5, name: 'Upma', cost: 20 },
    { id: 6, name: 'Chapati', cost: 20 },
    { id: 7, name: 'Bonda', cost: 20 },
    { id: 8, name: 'Vada', cost: 20 },
    { id: 9, name: 'Lemon Rice', cost: 30 },
    { id: 10, name: 'Tomato Rice', cost: 30 },
  ];

  const handleSelectionChange = (e) => {
    const selectedItem = items.find((item) => item.id === parseInt(e.target.value));
    setSelectedItem(selectedItem);
  };

  const addItem = () => {
    if (!selectedItem) {
      alert('Please select an item!');
      return;
    }

    const newTransaction = {
      id: transactions.length + 1,
      itemName: selectedItem.name,
      quantity: itemQuantity,
      costPerItem: selectedItem.cost,
    };

    setTransactions([...transactions, newTransaction]);
    setSelectedItem(null);
    setItemQuantity(1);
  };

  const calculateTotalCost = () => {
    return transactions.reduce((total, transaction) => total + transaction.quantity * transaction.costPerItem, 0);
  };

  const calculateGST = () => {
    const totalCost = calculateTotalCost();
    return (5 / 100) * totalCost;
  };

  const calculateBillAmount = () => {
    const totalCost = calculateTotalCost();
    const gst = calculateGST();
    return Math.ceil(totalCost + gst);
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="container">
      <h2 className="title">Puli'S Hotel Invoice</h2>
      <div className="dateTime">{currentDateTime.toLocaleString()}</div>
      <hr />

      <div className="form-group">
        <label htmlFor="item">Select Item:</label>
        <select
          id="item"
          className="form-control"
          onChange={handleSelectionChange}
          value={selectedItem ? selectedItem.id : ''}
        >
          <option value="">Select an item</option>
          {items.map((item) => (
            <option key={item.id} value={item.id}>
              {item.name}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="itemQuantity">Number of Selected Items:</label>
        <input
          type="number"
          id="itemQuantity"
          className="form-control"
          value={itemQuantity}
          onChange={(e) => setItemQuantity(parseInt(e.target.value))}
        />
      </div>

      <button className="btn btn-primary" onClick={addItem}>
        Add Item
      </button>

      <hr />

      <table className="table">
        <thead>
          <tr>
            <th>S.No.</th>
            <th>Item Name</th>
            <th>Item Quantity</th>
            <th>Cost Per Item</th>
            <th>Total Cost</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((transaction, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{transaction.itemName}</td>
              <td>{transaction.quantity}</td>
              <td>{transaction.costPerItem}</td>
              <td>{transaction.quantity * transaction.costPerItem}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div>Total Cost of Items: {calculateTotalCost()}</div>
      <div>GST (5%): {calculateGST()}</div>
      <div>Bill Amount: {calculateBillAmount()}</div>

      <div className="text-center mt-4">
        <button className="btn btn-primary" onClick={handlePrint}>
          Print
        </button>
      </div>
    </div>
  );
};

export default HotelBillScreen;
