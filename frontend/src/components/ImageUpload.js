import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload = () => {
  const [images, setImages] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [histogramPath, setHistogramPath] = useState(null);
  const [segmentationMask, setSegmentationMask] = useState(null);
  const [resizeParams, setResizeParams] = useState({ width: '', height: '' });
  const [cropParams, setCropParams] = useState({ left: '', top: '', right: '', bottom: '' });
  const [format, setFormat] = useState('JPEG');

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('images', selectedFile);

    try {
      const response = await axios.post('http://127.0.0.1:5000/images/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setImages([...images, { filename: selectedFile.name }]);
      setSelectedFile(null);
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  const fetchHistogram = async (filename) => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/images/histogram/${filename}`);
      console.log(response.request.responseURL)
      setHistogramPath(response.request.responseURL); // Use the response URL
    } catch (error) {
      console.error('Error fetching histogram:', error);
    }
  };

  const fetchSegmentationMask = async (filename) => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/images/segmentation/${filename}`);
      setSegmentationMask(response.request.responseURL);
    } catch (error) {
      console.error('Error fetching segmentation mask:', error);
    }
  };

  const handleResize = async (filename) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/images/resize', {
        filename,
        width: parseInt(resizeParams.width),
        height: parseInt(resizeParams.height),
      });
      alert(response.data.message);
    } catch (error) {
      console.error('Error resizing image:', error);
    }
  };

  const handleCrop = async (filename) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/images/crop', {
        filename,
        left: parseInt(cropParams.left),
        top: parseInt(cropParams.top),
        right: parseInt(cropParams.right),
        bottom: parseInt(cropParams.bottom),
      });
      alert(response.data.message);
    } catch (error) {
      console.error('Error cropping image:', error);
    }
  };

  const handleConvert = async (filename) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/images/convert', {
        filename,
        format,
      });
      alert(response.data.message);
    } catch (error) {
      console.error('Error converting image format:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload Image</button>

      <div>
        <h2>Uploaded Images</h2>
        <ul>
          {images.map((image, index) => (
            <li key={index}>
              {image.filename}
              <button onClick={() => fetchHistogram(image.filename)}>Get Histogram</button>
              <button onClick={() => fetchSegmentationMask(image.filename)}>Get Segmentation Mask</button>
              <div>
                <input
                  type="number"
                  placeholder="Width"
                  value={resizeParams.width}
                  onChange={(e) => setResizeParams({ ...resizeParams, width: e.target.value })}
                />
                <input
                  type="number"
                  placeholder="Height"
                  value={resizeParams.height}
                  onChange={(e) => setResizeParams({ ...resizeParams, height: e.target.value })}
                />
                <button onClick={() => handleResize(image.filename)}>Resize</button>
              </div>
              <div>
                <input
                  type="number"
                  placeholder="Left"
                  value={cropParams.left}
                  onChange={(e) => setCropParams({ ...cropParams, left: e.target.value })}
                />
                <input
                  type="number"
                  placeholder="Top"
                  value={cropParams.top}
                  onChange={(e) => setCropParams({ ...cropParams, top: e.target.value })}
                />
                <input
                  type="number"
                  placeholder="Right"
                  value={cropParams.right}
                  onChange={(e) => setCropParams({ ...cropParams, right: e.target.value })}
                />
                <input
                  type="number"
                  placeholder="Bottom"
                  value={cropParams.bottom}
                  onChange={(e) => setCropParams({ ...cropParams, bottom: e.target.value })}
                />
                <button onClick={() => handleCrop(image.filename)}>Crop</button>
              </div>
              <div>
                <select value={format} onChange={(e) => setFormat(e.target.value)}>
                  <option value="JPEG">JPEG</option>
                  <option value="PNG">PNG</option>
                </select>
                <button onClick={() => handleConvert(image.filename)}>Convert</button>
              </div>
            </li>
          ))}
        </ul>
      </div>

      {histogramPath && (
        <div>
          <h2>Color Histogram</h2>
          <img src={`${histogramPath}`} alt="Histogram" />
        </div>
      )}

      {segmentationMask && (
        <div>
          <h2>Segmentation Mask</h2>
          <img src={`${segmentationMask}`} alt="Segmentation Mask" />
        </div>
      )}
    </div>
  );
};

export default ImageUpload;
