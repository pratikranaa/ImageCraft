import React from 'react';

function Forms() {
 return (
  <div className="w-full h-96 bg-zinc-900 text-white">
 <form class="max-w-lg mx-auto">
  <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="image_detect">Upload file</label>
  <input class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="image_detect" type="file" />
</form>
</div>
)
};


export default Forms;