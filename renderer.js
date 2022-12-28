// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
const btn = document.getElementById('btn')
const filePathElement = document.getElementById('filePath')

// Hide things initially
document.getElementById('inprogress-msg').hidden = true;
document.getElementById('complete-msg').hidden = true;

btn.addEventListener('click', async () => {
  // Show the in-progress message
  document.getElementById('inprogress-msg').hidden = false
  const filePath = await window.electronAPI.openFile()

  // Show progress for at least .5 seconds
  window.setTimeout(function() {
    // Hide the in-progress message
    document.getElementById('inprogress-msg').hidden = true
    // Show the complete message
    document.getElementById('complete-msg').hidden = false
    filePathElement.innerText = filePath
  }, 500)
  
})