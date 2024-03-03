/**
 * Hash Set - seen dynamic
 * Time O(log(N)) | Space O(log(N))
 * https://leetcode.com/problems/happy-number/
 * @param {number} n
 * @return {boolean}
 */
var isHappy = (n, seen = new Set()) => {
  const hasCycle = () => n === 1 || seen.has(n);
  while (!hasCycle()) {
    /* Time O(log(N)) */
    seen.add(n); /* Space O(log(N)) */
    n = getNext(n); /* Time O(log(N)) */
  }

  return n === 1;
};

var getNext = (n, sum = 0) => {
  while (0 < n) {
    /* Time O(log(N)) */
    const remainder = n % 10;

    n = Math.floor(n / 10);
    sum += remainder * remainder;
  }

  return sum;
};
