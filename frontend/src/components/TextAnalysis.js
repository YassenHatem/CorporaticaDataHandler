import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const TextAnalysis = () => {
  const [texts, setTexts] = useState([]);
  const [formData, setFormData] = useState({ text: '' });
  const [tsneData, setTsneData] = useState([]);

  useEffect(() => {
    fetchTexts();
    fetchTsneData();
  }, []);

  const fetchTexts = async () => {
    try {
      const response = await api.get('/text/list');
      setTexts(response.data);
    } catch (error) {
      console.error('Error fetching texts:', error);
    }
  };

  const fetchTsneData = async () => {
    try {
      const response = await api.get('/text/tsne');
      setTsneData(response.data.map((point, index) => ({ x: point[0], y: point[1], index })));
    } catch (error) {
      console.error('Error fetching t-SNE data:', error);
    }
  };

  const handleInputChange = (e) => {
    setFormData({ ...formData, text: e.target.value });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      if (formData._id) {
        await api.put(`/text/update/${formData._id}`, formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      } else {
        await api.post('/text/create', formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      }
      setFormData({ text: '' });
      fetchTexts();
      fetchTsneData();
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  const handleEdit = (text) => {
    setFormData(text);
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/text/delete/${id}`, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      fetchTexts();
      fetchTsneData();
    } catch (error) {
      console.error('Error deleting text:', error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-xl font-bold mb-4">Text Analysis</h2>
      <form onSubmit={handleFormSubmit} className="mb-4">
        <textarea
          name="text"
          value={formData.text}
          onChange={handleInputChange}
          placeholder="Enter text here..."
          required
          className="p-2 border rounded w-full"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded mt-2">Submit</button>
      </form>
      <table className="table-auto w-full mt-4">
        <thead>
          <tr>
            <th className="px-4 py-2">Text</th>
            <th className="px-4 py-2">Summary</th>
            <th className="px-4 py-2">Keywords</th>
            <th className="px-4 py-2">Sentiment</th>
            <th className="px-4 py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          {texts.map((text) => (
            <tr key={text._id} className="hover:bg-gray-200">
              <td className="border px-4 py-2">{text.text}</td>
              <td className="border px-4 py-2">{text.summary}</td>
              <td className="border px-4 py-2">{text.keywords.join(', ')}</td>
              <td className="border px-4 py-2">{text.sentiment}</td>
              <td className="border px-4 py-2">
                <button onClick={() => handleEdit(text)} className="bg-green-500 text-white px-2 py-1 rounded mr-2">Edit</button>
                <button onClick={() => handleDelete(text._id)} className="bg-red-500 text-white px-2 py-1 rounded">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <h3 className="text-lg font-bold mt-4">t-SNE Visualization</h3>
      <ResponsiveContainer width="100%" height={400}>
        <ScatterChart>
          <CartesianGrid />
          <XAxis dataKey="x" name="X" />
          <YAxis dataKey="y" name="Y" />
          <Tooltip cursor={{ strokeDasharray: '3 3' }} />
          <Scatter name="Text Data" data={tsneData} fill="#8884d8" />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default TextAnalysis;
