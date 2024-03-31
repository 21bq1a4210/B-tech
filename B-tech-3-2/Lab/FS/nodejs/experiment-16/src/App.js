import React, { useState } from 'react';
import './App.css';

const FileHandlingApp = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleFileAction = (action) => {
    if (!file) {
      console.log('No file selected.');
      return;
    }

    switch (action) {
      case 'upload':
        console.log('File uploaded:', file);
        break;
      case 'download':
        const url = URL.createObjectURL(new Blob([file]));
        const link = document.createElement('a');
        link.href = url;
        link.download = file.name;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        break;
      default:
        break;
    }
  };

  return (
    <div className="container">
      <h1 style={{ borderBottom: '2px solid red', paddingBottom: '10px', marginBottom: '20px', color: 'indigo' }}>File Handling App</h1>
      <input type="file" onChange={handleFileChange} />
      <br />
      <button onClick={() => handleFileAction('upload')}>Upload File</button>
      <button onClick={() => handleFileAction('download')}>Download File</button>
      {file && (
        <div>
          <h3>File Preview</h3>
          {file.type.startsWith('image/') ? (
            <img src={URL.createObjectURL(file)} alt="File Preview" style={{ maxWidth: '300px', maxHeight: '300px', border: '1px solid #ddd' }} />
          ) : (
            <iframe title="file-preview" style={{ width: '100%', height: '300px', border: '1px solid #ddd' }} src={URL.createObjectURL(file)} />
          )}
        </div>
      )}
    </div>
  );
};

export default FileHandlingApp;