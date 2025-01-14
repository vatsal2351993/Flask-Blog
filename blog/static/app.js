
  // Set up the download button
  document.addEventListener('DOMContentLoaded', function () {
    const imageElement = document.getElementById('snippet-image');
    const downloadLink = document.getElementById('download-btn');
  
    // Set up the download button
    downloadLink.addEventListener('click', function (event) {
      event.preventDefault(); // Prevent default action
  
      const imageURL = imageElement.src; // Get the image URL
      const fileName = imageURL.split('/').pop(); // Extract the file name from the URL
  
      // Create a temporary <a> element to trigger the download
      const tempLink = document.createElement('a');
      tempLink.href = imageURL;
      tempLink.download = fileName; // Set the filename for download
      tempLink.style.display = 'none'; // Hide the link
      document.body.appendChild(tempLink);
  
      tempLink.click(); // Trigger the download
      document.body.removeChild(tempLink); // Remove the temporary link
    });
  });


