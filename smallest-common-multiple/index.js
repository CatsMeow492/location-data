function divisible(num) {
    for (let i = 0; i < num; i++) {
        if (num % i　== 0) {
            return true;
        }
    }
  }
  function smallestCommons(arr) {
    console.log(divisible(arr[1]))
    return arr;
  }
  
  
  smallestCommons([1,5]);