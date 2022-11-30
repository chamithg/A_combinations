function combine(n, k) {
  let output = [];

  function backTrack(start, comb) {
    // base case
    // check if the posible solution found
    if (comb.length === k) {
      output.push([...comb]); // make a copy of solution
      return;
    }

    // recursive funciton
    for (let i = start; i <= n; i++) {
      comb.push(i);

      // recurse
      backTrack(i + 1, comb);

      // backtrack
      comb.pop();
    }
  }

  backTrack(1, []);
  return output;
}

let n = 4;
let k = 2;

console.log(combine(n, k));
