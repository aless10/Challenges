/*
You are provided a string containing a list of positive integers separated by a space (" "). Take each value and calculate the sum of its digits, which we call it's "weight". Then return the list in ascending order by weight, as a string joined by a space.

For example 99 will have "weight" 18, 100 will have "weight"
1 so in the ouput 100 will come before 99.

Example:

  "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
  "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let's consider them to be strings and not numbers:

100 is before 180 because its "weight" (1) is less than the one of 180 (9)
and 180 is before 90 since, having the same "weight" (9) it comes before as a string.

  All numbers in the list are positive integers and the list can be empty.*/


function orderWeight(strng) {
  // 1. split the string to a list of integers
  let arr = strng.split(" ")
  // 2. for each element, use reduce to get the sum of the digits
  let arrDigits = arr
    .map(
      (v, i) => [ arr[i], v.split('')
        .map(Number)
        .reduce(
          function (a, b) {
            return a + b;
          }, 0) ])
  // 3. order the array by this value
  arrDigits.sort(function (a, b) {
    return a[1] - b[1] !== 0 ? a[1] - b[1] : a[0].localeCompare(b[0]);
  });
  // 4. join the array of values by " "
  return arrDigits.map(el => el[0]).join(" ")
}

console.log(orderWeight("56 65 74 100 99 68 86 180 90"))
