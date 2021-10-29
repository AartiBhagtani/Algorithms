var io = require('socket.io-client');
var socket = io.connect('http://localhost:4000/', {reconnect: true});

socket.on('connect', function (socket) {
    console.log('Connected!');
});

socket.on('sendLogs', function (text) {
  console.log(text);
})

// const http = require('http')

// const app = express()

// let server = http.createServer(app)
// let io = socketIO(server)

// app.get('/', (req, res) => {
//   res.send('Welcome')
// })

// app.get('/log', logController.show_logs)

// // app.listen(3000, () => {
// //   console.log('app started')
// // })

// server.listen(3000);

// io.on('connection', (socket)=>{
//   console.log('New user connected');
//   socket.on('sendLogs', function(logText){
//     console.log(logText)
//   })
// })
