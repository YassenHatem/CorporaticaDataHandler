
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TabularData = () => {
  const [data, setData] = useState([]);
  const [formData, setFormData] = useState({_id: '', name: '', value: '' });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const response = await axios.get('http://127.0.0.1:5000/tabular/read');
    setData(response.data);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    if (formData._id) {
      await axios.put('http://127.0.0.1:5000/tabular/update', formData);
    } else {
      await axios.post('http://127.0.0.1:5000/tabular/create', formData);
    }
    setFormData({ _id: '', name: '', value: '' });
    fetchData();
  };

  const handleEdit = (record) => {
    setFormData(record);
  };

  const handleDelete = async (id) => {
    await axios.delete('http://127.0.0.1:5000/tabular/delete', formData);
    fetchData();
  };

  return (
    <div>
      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleInputChange}
          placeholder="Name"
          required
        />
        <input
          type="number"
          name="value"
          value={formData.value}
          onChange={handleInputChange}
          placeholder="Value"
          required
        />
        <button type="submit">Submit</button>
      </form>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Value</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {data.map((record) => (
            <tr key={record._id}>
              <td>{record.name}</td>
              <td>{record.value}</td>
              <td>
                <button onClick={() => handleEdit(record)}>Edit</button>
                <button onClick={() => handleDelete(record)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TabularData;
