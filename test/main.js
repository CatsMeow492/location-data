const person = function(name, last, id) {
    firstName: name,
    lastName: last,
    id: id,
    fullName: function() {
      return this.firstName + " " + this.lastName;
    }
  };
  
  let me = new person('Taylor', 'Mohney', '1955')