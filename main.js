// Modules to control application life and create native browser window
const {app, BrowserWindow, ipcMain, dialog} = require('electron')
const path = require('path')
const util = require('util');
const fs = require('fs');
const exec = util.promisify(require('child_process').exec);
var mainWindow;

async function generateCLOBotScript(e, blocksFolderPath, outputFolderPath, scriptOutputFolderPath) {
  console.log('Testing arguments', blocksFolderPath, outputFolderPath, scriptOutputFolderPath);

  var processName = path.join(app.getAppPath(), 'clobot/clobot.exe');

  // When testing on a mac, run the python script directly.
  if (process.platform === 'darwin') {
    processName = 'python3 ' + path.join(app.getAppPath(), 'clobot/main.py');
  }
  console.log('process name: ', processName)
  const { stdout, stderr } = await exec(processName + ' ' + 
    blocksFolderPath + ' ' +
    outputFolderPath + ' ' +
    scriptOutputFolderPath
  );

  if (stderr) {
    console.error(`error: ${stderr}`);
  }
  console.log(`${stdout}`);
  return stdout;
}

async function handleFileOpen() {
  const { canceled, filePaths } = await dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory']
  })
  if (canceled) {
    return
  } else {;
    return filePaths[0]
  }
}

async function getDefaultPaths() {
  var macDefaultPaths = [
    '/Applications/CLO_Network_OnlineAuth.app/Contents/Assets/Blocks/Woman/Polos',
    app.getPath("temp") + 'clobot/output',
    app.getPath("temp") + 'clobot.py'
  ];

  var winDefaultPaths = [
    'C:\\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos',
    'C:\\Users\Public\Documents\CLO',
    'C:\\Users\Public\Documents\CLO\clobot.py'
  ];

  if (process.platform === 'darwin') {
    return macDefaultPaths;
  }
  else {
    return winDefaultPaths;
  }
}

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')

  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  
  ipcMain.handle('generateCLOBotScript', generateCLOBotScript)
  ipcMain.handle('handleFileOpen', handleFileOpen)
  ipcMain.handle('getDefaultPaths', getDefaultPaths)

  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
