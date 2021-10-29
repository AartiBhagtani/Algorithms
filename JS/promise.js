let p = new Promise((resolve, reject) => {
  const a =  1 + 1;
  if (a == 2) {
    resolve('success')
  } 
  else {
    reject('failure')
  }
})

p.then((message) => {
  console.log(message)
}).cath((message) => {
  console.log(message)
})

// function is just a variable
function printName() {
  console.log('m in function')
}

console.log(printName())

setTimeout(() => {
  console.log('I m inline function')
}, 1000)

// function as a 