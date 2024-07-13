import React, { useState } from 'react';
import api from '../services/api';
import { motion } from 'framer-motion';

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
      await api.post('/images/upload', formData, {
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
      const response = await api.get(`/images/histogram/${filename}`);
      setHistogramPath(response.request.responseURL);
    } catch (error) {
      console.error('Error fetching histogram:', error);
    }
  };

  const fetchSegmentationMask = async (filename) => {
    try {
      const response = await api.get(`/images/segmentation/${filename}`);
      setSegmentationMask(response.request.responseURL);
    } catch (error) {
      console.error('Error fetching segmentation mask:', error);
    }
  };

  const handleResize = async (filename) => {
    try {
      const response = await api.post('/images/resize', {
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
      const response = await api.post('/images/crop', {
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
      const response = await api.post('/images/convert', {
        filename,
        format,
      });
      alert(response.data.message);
    } catch (error) {
      console.error('Error converting image format:', error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <div className="mb-4">
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload} className="ml-2 bg-blue-500 text-white p-2 rounded">
          Upload Image
        </button>
      </div>

      <motion.div
        className="uploaded-images"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        <h2 className="text-xl font-bold">Uploaded Images</h2>
        <ul>
          {images.map((image, index) => (
            <li key={index} className="mb-2">
              {image.filename}
              <button onClick={() => fetchHistogram(image.filename)} className="ml-2 bg-green-500 text-white p-1 rounded">
                Get Histogram
              </button>
              <button onClick={() => fetchSegmentationMask(image.filename)} className="ml-2 bg-purple-500 text-white p-1 rounded">
                Get Segmentation Mask
              </button>
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
                <button onClick={() => handleResize(image.filename)} className="ml-2 bg-yellow-500 text-white p-1 rounded">
                  Resize
                </button>
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
                <button onClick={() => handleCrop(image.filename)} className="ml-2 bg-red-500 text-white p-1 rounded">
                  Crop
                </button>
              </div>
              <div>
                <select value={format} onChange={(e) => setFormat(e.target.value)}>
                  <option value="JPEG">JPEG</option>
                  <option value="PNG">PNG</option>
                </select>
                <button onClick={() => handleConvert(image.filename)} className="ml-2 bg-indigo-500 text-white p-1 rounded">
                  Convert
                </button>
              </div>
            </li>
          ))}
        </ul>
      </motion.div>

      {histogramPath && (
        <motion.div
          className="histogram"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <h2 className="text-xl font-bold">Color Histogram</h2>
          <img src={histogramPath} alt="Histogram" />
        </motion.div>
      )}

      {segmentationMask && (
        <motion.div
          className="segmentation-mask"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <h2 className="text-xl font-bold">Segmentation Mask</h2>
          <img src={`${segmentationMask}`} alt="Segmentation Mask" />
        </motion.div>
      )}
    </div>
  );
};

export default ImageUpload;
