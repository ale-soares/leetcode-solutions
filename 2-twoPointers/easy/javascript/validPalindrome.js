/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let clean = s.replace(/[^a-z0-9]/gi, "").toLowerCase();
  if (clean.length === 0) return true;

  let left = 0;
  let right = clean.length - 1;

  for (let i = 0; i < clean.length; i++) {
    if (clean[left] !== clean[right]) return false;

    left++;
    right--;
  }

  return true;
};
