import React from 'react';
import { BrowserRouter as Router, Route, Routes, NavLink } from 'react-router-dom';
import ImageUpload from './components/ImageUpload';
import TabularData from './components/TabularData';
import TextAnalysis from './components/TextAnalysis';

const App = () => {
  return (
    <Router>
      <div className="container mx-auto p-4">
        <nav className="mb-4">
          <NavLink to="/" exact className={({ isActive }) => (isActive ? 'mr-4 font-bold' : 'mr-4')}>
            Home
          </NavLink>
          <NavLink to="/images" className={({ isActive }) => (isActive ? 'mr-4 font-bold' : 'mr-4')}>
            Images
          </NavLink>
          <NavLink to="/data" className={({ isActive }) => (isActive ? 'mr-4 font-bold' : 'mr-4')}>
            Data
          </NavLink>
          <NavLink to="/text" className={({ isActive }) => (isActive ? 'font-bold' : '')}>
            Text
          </NavLink>
        </nav>

        <Routes>
          <Route path="/" exact element={<h1 className="text-2xl font-bold">Welcome to the Enhanced UI Application</h1>} />
          <Route path="/images" element={<ImageUpload />} />
          <Route path="/data" element={<TabularData />} />
          <Route path="/text" element={<TextAnalysis />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
