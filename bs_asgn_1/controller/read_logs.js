const fs = require('fs')
const file_path = '/Users/aartibhagtani/Documents/P/bs_asgn_1/files/logs.log'

exports.get_logs = (req, res, next) => {
  fs.readFile(file_path, (err, data) => {
    file_data = data.toString()
    fs.watch(file_path, (event, file_name) => {
      console.log("\nThe file", file_name, "was modified! with event", event);
      file_data = data.toString()
    })
    res.send(file_data)
  })  
};
