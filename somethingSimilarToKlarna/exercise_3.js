/*Task
We are tracking down our rogue agent and she travels from place to place to avoid being tracked. Each of her travels are based on a list of itineraries in an unusual or incorrect order. The task is to determine the complete route she will take.

  You are given an array of routes containing her travel itineraries. Convert this into a complete, in-order list of the places she will travel.

 Specification
  findRoutes(routes)
  Parameters
  routes: Array<Array<String>> - Array of itineraries

  Return Value
  String - An ordered list or destinations

Constraints
All inputs have at least one valid, complete route

Examples
routes
  [["USA","BRA"],["JPN","PHL"],["BRA","UAE"],["UAE","JPN"]]
Return Value
 "USA, BRA, UAE, JPN, PHL"
  */


/*
function findRoutes(routes) {
  let completeRoute = []
  for (let route of routes) {
    let i = completeRoute.indexOf(route[0])
    let j = completeRoute.indexOf(route[1])
    if (i === -1 && j === -1) {
      completeRoute.push(...route)
    } else if (i !== -1 && j === -1) {
      completeRoute.splice(i, 1, ...route);
    } else if (i === -1 && j !== -1) {
      completeRoute.splice(j, 1, ...route);
    } else if (i !== -1 && j === 0) {
      completeRoute.splice(i, 1, ...route);
      completeRoute.shift()
      let partialDestination = completeRoute.shift()
      completeRoute.push(partialDestination)
    } else {
      completeRoute.splice(i, 1, ...route);
    }
  }
  const uniqueCompleteRoute = completeRoute.filter(function(elem, pos) {
    return completeRoute.indexOf(elem) === pos;
  })
  return uniqueCompleteRoute.join(", ")
}
*/

function findRoutes(routes) {
  let copyRoute = {}
  let start = []
  for (let route of routes) {
    let [ from, to ] = route
    if (copyRoute[from] === undefined) {
      start.push(...route)
      copyRoute[from] = {
        before: null,
        after: to
      }
    } else {
      copyRoute[from].after = to
    }
    if (copyRoute[to] === undefined) {
      copyRoute[to] = {
        before: from,
        after: null
      }
    } else {
      copyRoute[to].before = from
      const index = start.indexOf(to);
      if (index > -1) {
        start.splice(index, 2);
      }
    }
  }
  let nextElement = copyRoute[start[0]].after
  delete copyRoute[start[0]]
  while (nextElement !== null) {
    start.push(copyRoute[start[start.length - 1]].after)
    nextElement = copyRoute[start[start.length - 2]].after
    delete copyRoute[start[start.length - 2]]
  }
  return start.filter((v) => v !== null).join(", ")

}


/*console.log(findRoutes([
    [ "Chicago", "Winnipeg" ],
    [ "Winnipeg", "Seattle" ],
    [ "Halifax", "Montreal" ],
    [ "Montreal", "Toronto" ],
    [ "Toronto", "Chicago" ]
  ]
))*/


/*
console.log(findRoutes([
  ["Chicago", "Winnipeg"],
  ["Halifax", "Montreal"],
  ["Montreal", "Toronto"],
  ["Toronto", "Chicago"],
  ["Winnipeg", "Seattle"]]
))
*/

console.log(findRoutes([["USA","BRA"],["JPN","PHL"],["BRA","UAE"],["UAE","JPN"]]))
//console.log(findRoutes([["BRA","UAE"],["USA","BRA"],["JPN","PHL"],["UAE","JPN"]]))

//console.log(findRoutes([["MNL", "TAG"], ["CEB", "TAC"], ["TAG", "CEB"], ["TAC", "BOR"]]))
// "MNL, TAG, CEB, TAC, BOR"

