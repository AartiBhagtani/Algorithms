// normal functions. 
function is_positive(number) {
  return number > 0;
}

let is_positive = (number) => {
  return number > 0
}

const is_positive_ = (number) => number > 0

let is_positive = number => number > 0

function get_sum(a, b) {
  return a + b;
}

let get_sum = (a, b) => {
  return a + b
}

let get_sum  = (a, b ) => a + b

function get_random() {
  return Math.random;
}

let get_random = () => Math.random

// annonymous function
document.addEventListener('click', function() {
  console.log('click')
})

document.addEventListener('click', () => {
  console.log('click')
})