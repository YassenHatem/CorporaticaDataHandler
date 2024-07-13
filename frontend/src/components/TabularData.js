import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TabularData = () => {
  const [data, setData] = useState([]);
  const [formData, setFormData] = useState({ name: '', value: '' });

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
    console.log(formData)
    if (formData.id) {
      await axios.put('http://127.0.0.1:5000/tabular/update', formData, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    } else {
      await axios.post('http://127.0.0.1:5000/tabular/create', formData, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    }
    setFormData({ name: '', value: '' });
    fetchData();
  };

  const handleEdit = (record) => {
    setFormData(record);
  };

  const handleDelete = async (id) => {
    console.log(id)
    await axios.delete('http://127.0.0.1:5000/tabular/delete', {
      headers: {
        'Content-Type': 'application/json'
      },
      data: { _id: id }
    });
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
            <tr key={record.id}>
              <td>{record.name}</td>
              <td>{record.value}</td>
              <td>
                <button onClick={() => handleEdit(record)}>Edit</button>
                <button onClick={() => handleDelete(record.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TabularData;
