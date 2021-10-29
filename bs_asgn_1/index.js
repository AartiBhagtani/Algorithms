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
  fs.watch(file_path, async (event, file_name) => {
    console.log("\nThe file", file_name, "was modified! with event", event);
    fs.readFile(file_path, (err, data) => {
      let file_data = data.toString()
      // return file_data
      socket.emit('sendLogs', {
        text: file_data
      })
    })  
  })
}

