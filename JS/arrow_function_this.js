class Person {
  constructor(name) {
    this.name = name
  }

  printName() {
    setTimeout(() => {
      console.log(this.name)
    }, 1000)
  }
}

let person = new Person('bob')

person.printName()