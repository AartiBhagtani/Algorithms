const get_details_button = document.getElementById('details')
const a = 3;

function callEvent() {
  return new Promise((resolve, reject) => {
    if(a == 2) {
      resolve('successful')
    }
    else {
      reject('failure')
    }
  })
}

async function doWork() {
  try {
    const response = await callEvent()
    console.log(response)
  }
  catch(err) {
    console.log(err)
  }
}

doWork()
