
import React from 'react';
import TabularData from './components/TabularData';
import ImageUpload from './components/ImageUpload';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Corporatica Data Handler</h1>
      </header>
      <TabularData />
        <ImageUpload />
    </div>
  );
};

export default App;
