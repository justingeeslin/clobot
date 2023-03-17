// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
const btn = document.getElementById('btn')

//Set default paths
const defaultPathsPromise = window.electronAPI.getDefaultPaths();
defaultPathsPromise.then((defaultPaths) => {
  console.log('Default paths', defaultPaths);
  document.getElementById('blocks-folder-path').innerText = defaultPaths[0];
  document.getElementById('output-folder-path').innerText = defaultPaths[1];
  document.getElementById('python-output-folder-path').innerText = defaultPaths[2];
}).catch(err=>console.log(err))


// Hide progress bars initially
document.getElementById('inprogress-msg').hidden = true;
document.getElementById('complete-msg').hidden = true;

btn.addEventListener('click', async () => {
  // Show the in-progress message
  document.getElementById('inprogress-msg').hidden = false

  // Get the folder paths as arguments
  const blocksFolderPath = document.getElementById('blocks-folder-path').innerText;
  const outputFolderPath = document.getElementById('output-folder-path').innerText;
  const scriptOutputFolderPath = document.getElementById('python-output-folder-path').innerText;

  const filePath = await window.electronAPI.generateCLOBotScript(blocksFolderPath, outputFolderPath, scriptOutputFolderPath);

  // Add the path append command to the UI since this varies on user input
  document.getElementById('path-append').innerText = 'sys.path.append(r"' + scriptOutputFolderPath.replace('/clobot.py', '') + '")'

  // Show progress for at least .5 seconds
  window.setTimeout(function() {
    // Hide the in-progress message
    document.getElementById('inprogress-msg').hidden = true
    // Show the complete message
    document.getElementById('complete-msg').hidden = false
    filePathElement.innerText = filePath
  }, 500)
  
});


const inputFileBlocksFolder = document.getElementById('blocks-folder');
inputFileBlocksFolder.addEventListener('click', async () => {
  const chosenDirectory = await window.electronAPI.handleFileOpen();
  const filePathElement = document.getElementById('blocks-folder-path')
  filePathElement.innerText = chosenDirectory;
})

const pythonOutputFileBlocksFolder = document.getElementById('python-output-folder');
pythonOutputFileBlocksFolder.addEventListener('click', async () => {
  const chosenDirectory = await window.electronAPI.handleFileOpen();
  const filePathElement = document.getElementById('python-output-folder-path')
  filePathElement.innerText = chosenDirectory;
})

const outputFileBlocksFolder = document.getElementById('output-folder');
outputFileBlocksFolder.addEventListener('click', async () => {
  const chosenDirectory = await window.electronAPI.handleFileOpen();
  const filePathElement = document.getElementById('output-folder-path')
  filePathElement.innerText = chosenDirectory;
})

// ipc.on("path:selected", (event, path) => {
//   chosenPath = path;
//   console.log("Full path: ", chosenPath[0]);
// });

/* BOOTSTRAP TABS */
const triggerTabList = document.querySelectorAll('#myTab button')
triggerTabList.forEach(triggerEl => {
  const tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', event => {
    event.preventDefault()
    tabTrigger.show()
  })
})

/* Custom function for nexting */
const triggerEl = document.querySelector('#myTab button[data-bs-target="#profile"]')
bootstrap.Tab.getInstance(triggerEl).show() 