import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, BarChart, Bar, PieChart, Pie, Cell } from 'recharts';
import { motion } from 'framer-motion';

const TabularData = () => {
  const [data, setData] = useState([]);
  const [formData, setFormData] = useState({ name: '', value: '' });
  const [selectedData, setSelectedData] = useState(null);
  const [chartType, setChartType] = useState('line');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await api.get('/tabular/read');
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      if (formData.id) {
        await api.put('/tabular/update', formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      } else {
        await api.post('/tabular/create', formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      }
      setFormData({ name: '', value: '' });
      fetchData();
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  const handleEdit = (record) => {
    setFormData(record);
  };

  const handleDelete = async (id) => {
    try {
      await api.delete('/tabular/delete', {
        headers: {
          'Content-Type': 'application/json'
        },
        data: { _id: id }
      });
      fetchData();
    } catch (error) {
      console.error('Error deleting record:', error);
    }
  };

  const renderChart = () => {
    switch (chartType) {
      case 'bar':
        return (
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="value" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        );
      case 'pie':
        return (
          <ResponsiveContainer width="100%" height={400}>
            <PieChart>
              <Pie data={data} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={150} fill="#8884d8" label>
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color || '#8884d8'} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        );
      default:
        return (
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="value" stroke="#8884d8" activeDot={{ r: 8 }} />
            </LineChart>
          </ResponsiveContainer>
        );
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-xl font-bold mb-4">Tabular Data</h2>

      <motion.form onSubmit={handleFormSubmit} className="mb-4" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleInputChange}
          placeholder="Name"
          required
          className="p-2 border rounded mr-2"
        />
        <input
          type="number"
          name="value"
          value={formData.value}
          onChange={handleInputChange}
          placeholder="Value"
          required
          className="p-2 border rounded mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">Submit</button>
      </motion.form>

      <div className="mb-4">
        <label className="mr-2">Select Chart Type:</label>
        <select value={chartType} onChange={(e) => setChartType(e.target.value)} className="p-2 border rounded">
          <option value="line">Line Chart</option>
          <option value="bar">Bar Chart</option>
          <option value="pie">Pie Chart</option>
        </select>
      </div>

      {renderChart()}

      <motion.table className="table-auto w-full mt-4" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
        <thead>
          <tr>
            <th className="px-4 py-2">Name</th>
            <th className="px-4 py-2">Value</th>
            <th className="px-4 py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          {data.map((record) => (
            <tr key={record.id} className="hover:bg-gray-200">
              <td className="border px-4 py-2">{record.name}</td>
              <td className="border px-4 py-2">{record.value}</td>
              <td className="border px-4 py-2">
                <button onClick={() => handleEdit(record)} className="bg-green-500 text-white px-2 py-1 rounded mr-2">Edit</button>
                <button onClick={() => handleDelete(record.id)} className="bg-red-500 text-white px-2 py-1 rounded">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </motion.table>

      {selectedData && (
        <motion.div className="mt-4" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
          <h3 className="text-lg font-bold">Selected Data</h3>
          <p>Name: {selectedData.name}</p>
          <p>Value: {selectedData.value}</p>
        </motion.div>
      )}
    </div>
  );
};

export default TabularData;
