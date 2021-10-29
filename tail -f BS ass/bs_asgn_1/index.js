const express = require('express')

// const logController = require('./controller/read_logs.js')

const socketIO = require('socket.io');
const http = require('http')

const app = express()

let server = http.createServer(app)
let io = socketIO(server)

const fs = require('fs')
const file_path = '/Users/aartibhagtani/Documents/P/bs_asgn_1/files/logs.log'


app.get('/', (req, res) => {
  res.send('Welcome')
})

// app.get('/log', logController.get_logs)

server.listen(4000);

io.on('connection', (socket)=>{
  console.log('New user connected');
  readLogs(socket)
  console.log('emmitted event')
})


function readLogs(socket) {
  fs.watch(file_path, (event, file_name) => {
    console.log("\nThe file", file_name, "was modified! with event", event);
    file_data = read_file()
    console.log(file_data, 'data')
    socket.emit('sendLogs', {
      text: file_data
    })
  })
}

function read_file() {
  let file_data;
  fs.readFile(file_path, (err, data) => {
    file_data = data.toString()
    return file_data
  })  
  console.log(file_data)
}
