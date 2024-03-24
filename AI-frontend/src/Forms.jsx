import React, {useState} from 'react';
import { useRef } from "react";
import axios from 'axios';
import LoadingBar from "react-top-loading-bar";

function Forms() {
  const [image, setImage] = useState();
  const [data, setData] = useState(null);
  const formRef = React.createRef();
  const fileInputRef = React.createRef();

  function handleChange(e) {
      console.log(e.target.files);
      if(e.target.files[0]) {
        setImage(URL.createObjectURL(e.target.files[0]));
      } else {
        setImage(null);
      }
  }

  
  function handleSubmit(e) {
    e.preventDefault();
  
    if (fileInputRef.current.files[0]) {
      const formData = new FormData();
      formData.append('image', fileInputRef.current.files[0]);
  
      // Start the loading bar
      ref.current.continuousStart();
  
      axios.post('http://localhost:5000/api/process_images', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => {
        setData(response.data);
  
        // Set the image state with the base64 string from the response
        setImage(response.data.image);
  
        // Stop the loading bar
        ref.current.complete();
      }).catch(error => {
        console.log('Error:', error);
  
        // Stop the loading bar in case of error
        ref.current.complete();
      });
    } else {
      console.log('No file selected');
    }
  }

  
  function handleClear() {
    setImage(null);
    setData(null);
    formRef.current.reset();
  }

    // Count the number of each object
    const counts = {};

    if (data) {
        data.detection.forEach(detection => {
            if (counts[detection.name]) {
                counts[detection.name]++;
            } else {
                counts[detection.name] = 1;
            }
        });
    }


  const ref = useRef(null);

  const handleLoadSomething = () => {
    if (!image) {
      alert('No image selected');
      // or show an alert to the user
      // alert('No image selected');
    }
  };
  
  return (
        <div className="flex w-full h-screen bg-gray-800 text-white p-10">
              <div> <LoadingBar color="blue" ref={ref} /> </div>
          <div className="w-1/2">
        <h1 className="text-3xl font-bold text-center">Upload Image</h1>
        <form ref={formRef} onSubmit={handleSubmit} className="max-w-lg mx-auto">
         <label className="block mb-2 py-2 text-sm font-medium text-gray-900 dark:text-white">Please Upload the file for object detection.</label>
         <input ref={fileInputRef} className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="image_detect" type="file" onChange={handleChange} />
         <div className="flex justify-between mt-4">
         <button className="block w-1/2 py-2 text-sm font-semibold text-white bg-red-500 rounded-lg cursor-pointer hover:bg-red-400 focus:outline-none mr-2" type="button" onClick={handleClear}>Clear</button>
          <button className="block w-1/2 py-2 text-sm font-semibold text-white bg-gray-900 rounded-lg cursor-pointer hover:bg-gray-600 focus:outline-none ml-2" onClick={handleLoadSomething} type="submit">Upload</button>
          </div>
          {image && (
            <>
              <h2 className="block py-4 text-3xl font-bold text-center">Image to Upload</h2>
              <img className='p-2' src={image} style={{maxWidth: '100%', height: 'auto'}} />
            </>
          )}
       </form>
        </div>
<div className='w-1/2'>
  <h2 className="block py-4 text-3xl font-bold text-center">Output</h2>
  <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
      <tbody>
        {data ? (
          <>
            <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
              <th scope="row" className="px-6 py-4 dark:bg-gray-700 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                Captioning
              </th>
              <td className="px-6 py-4 dark:text-white">{data.captioning}</td>
            </tr>
            <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
              <th scope="row" className="px-6 py-4 dark:bg-gray-700 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                Classification
              </th>
              <td className="px-6 py-4 dark:text-white">{data.classification}</td>
            </tr>
            {data.detection.map((detection, index) => (
              <tr key={index} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                <th scope="row" className="px-6 py-4 dark:bg-gray-700 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                  Detection No. {index + 1}
                </th>
                <td className="px-6 py-4 dark:text-white ">
                  Count: {counts[detection.name]} | Object: {detection.name}
                </td>
              </tr>
            ))}
          </>
        ) : (
          <tr>
            <td className="px-6 py-4 dark:text-white text-bold dark:bg-gray-900">Please Upload an Image</td>
          </tr>
        )}
      </tbody>
    </table>
  </div>
</div>
       </div>
  );
                    }


export default Forms;