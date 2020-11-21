export const shiftedDiff = (first, second) => {
  const firstL = first.length
  const secondL = second.length
  if (firstL !== secondL) return -1
  let firstArr = Array.from(first)

  for (let i = 0; i < secondL; i++) {
    if (firstArr.join('') === second) return i
    let lastLetter = firstArr.pop()
    firstArr.unshift(lastLetter)
  }
  return -1;
};
