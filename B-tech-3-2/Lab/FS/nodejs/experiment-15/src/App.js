import React, { useState } from 'react';

const ImageTable = ({ selectedImages }) => (
  <div className="table-container">
    <table className="styled-table">
      <thead>
        <tr>
          <th style={tableHeaderStyle}>Image</th>
          <th style={tableHeaderStyle}>Name</th>
        </tr>
      </thead>
      <tbody>
        {selectedImages.map((image, index) => (
          <tr key={index}>
            <td><img src={image.src} alt={image.alt} style={imageStyle} /></td>
            <td>{image.alt}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

const App = () => {
  const [selectedImages, setSelectedImages] = useState([]);

  const handleFileUpload = (event) => {
    Array.from(event.target.files).forEach((file) => {
      const reader = new FileReader();
      reader.onload = () => setSelectedImages((prev) => [...prev, { src: reader.result, alt: file.name }]);
      reader.readAsDataURL(file);
    });
  };

  return (
    <div>
      <h1 style={headerStyle}>Dynamic Image Selection - Table</h1>
      <div className="upload-container">
        <input type="file" onChange={handleFileUpload} multiple />
        <ImageTable selectedImages={selectedImages} />
      </div>
      <div className="watermark">SHESANK</div>
    </div>
  );
};

const tableHeaderStyle = { border: '1px solid #3824ee', padding: '8px', textAlign: 'center', backgroundColor: 'lightblue' };
const imageStyle = { maxWidth: '100px', maxHeight: '100px' };
const headerStyle = { borderBottom: '2px solid blue', paddingTop: '20px', marginBottom: '100px' };

export default App;
