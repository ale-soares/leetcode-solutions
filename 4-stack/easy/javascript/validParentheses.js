/**
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/valid-parentheses/
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const parentheses = {
    "{": "}",
    "(": ")",
    "[": "]",
  };

  const stack = [];

  for (const char of s) {
    // If the character is an opening bracket, push it onto the stack
    if (Object.keys(parentheses).includes(char)) stack.push(char);
    // If the character is a closing bracket, pop from the stack and check if it matches
    // If not, or if the stack is empty, the string is invalid
    else if (parentheses[stack.pop()] !== char) return false;
  }

  // If the stack is empty, all brackets were properly closed
  return stack.length === 0;
};
