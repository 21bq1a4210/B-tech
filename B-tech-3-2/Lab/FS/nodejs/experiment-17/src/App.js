import React, { useState } from 'react';
import { Container, Form, Button, Card, Row, Col, Table } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
// import { saveAs } from 'file-saver';

function App() {
  const [formData, setFormData] = useState({
    principal: '',
    interestRate: '',
    loanTerm: ''
  });
  const [emi, setEmi] = useState([]);
  const [totalPayment, setTotalPayment] = useState(0);
  const [monthlyPayment, setMonthlyPayment] = useState(0);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const calculateEmi = () => {
    const { principal, interestRate, loanTerm } = formData;
    let p = parseFloat(principal);
    const r = parseFloat(interestRate) / 100 / 12;
    const n = parseFloat(loanTerm) * 12;

    const emiValue = (p * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
    setMonthlyPayment(emiValue.toFixed(2));

    const totalAmount = emiValue * n;
    setTotalPayment(totalAmount.toFixed(2));

    setEmi(Array.from({ length: n }, (_, i) => {
      const interestPayment = p * r;
      const principalPayment = emiValue - interestPayment;
      p -= principalPayment;

      return {
        month: i + 1,
        principal: principalPayment.toFixed(2),
        interest: interestPayment.toFixed(2),
        balance: p.toFixed(2),
      };
    }));
  };

  return (
    <Container className="mt-2">
      <Card className="calculator-card">
        <Card.Body>
          <Card.Title className="text-center">EMI Calculator</Card.Title>
          <Form>
            <Form.Group>
              <Form.Label>Loan Amount (Principal):</Form.Label>
              <Form.Control
                type="number"
                name="principal"
                placeholder="Enter loan amount"
                value={formData.principal}
                onChange={handleInputChange}
              />
            </Form.Group>
            <Form.Group>
              <Form.Label>Annual Interest Rate(%):</Form.Label>
              <Form.Control
                type="number"
                name="interestRate"
                placeholder="Enter annual interest rate"
                value={formData.interestRate}
                onChange={handleInputChange}
              />
            </Form.Group>
            <Form.Group>
              <Form.Label>Loan Term (Years):</Form.Label>
              <Form.Control
                type="number"
                name="loanTerm"
                placeholder="Enter loan term in years"
                value={formData.loanTerm}
                onChange={handleInputChange}
              />
            </Form.Group>
            <div className="d-flex justify-content-center mt-4">
              <Button variant="primary" className="small-button" onClick={calculateEmi} style={{ marginRight: '5px' }}>
                Calculate EMI
              </Button>
            </div>
          </Form>
          {totalPayment !== 0 && monthlyPayment !== 0 && (
            <div className="mt-4">
              <Row>
                <Col xs={6} className="text-right">
                  <h6 style={{ color: 'red' }}>EMI:</h6>
                </Col>
                <Col xs={6} className="text-left">
                  <h6 style={{ color: 'red' }}>₹ {(+monthlyPayment).toLocaleString('en-IN', { maximumFractionDigits: 2 })} /- <br></br>(per Month)</h6>
                </Col>
              </Row>
            </div>
          )}
        </Card.Body>
      </Card>

      {emi.length > 0 && (
        <div className="mt-4" style={{ overflowY: 'auto', maxHeight: '570px' }}>
          <h5 className="text-center">EMI Statement</h5>
          <Table striped bordered hover size="sm" className="text-center table-sm-font-size">
            <thead>
              <tr>
                <th>Month</th>
                <th>Principal</th>
                <th>Interest</th>
                <th>Loan Outstanding</th>
              </tr>
            </thead>
            <tbody>
              {emi.map((entry) => (
                <tr key={entry.month}>
                  <td>{entry.month}</td>
                  <td>₹ {Math.floor(entry.principal)}</td>
                  <td>₹ {Math.floor(entry.interest)}</td>
                  <td>₹ {Math.floor(entry.balance)}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </div>
      )}
    </Container>
  );
}

export default App;