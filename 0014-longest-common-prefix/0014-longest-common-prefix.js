/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  if (strs.length === 1) {
    return strs[0];
  }

  const start = [];
  let startIndex = 0;

  while (strs.every((str) => {
    for (const index in start) {
      if (str[index] !== start[index]) {
        return false
      }
    }

    return true 
  })) {
    if (startIndex === strs[0].length) {
      return start.join("");
    }

    start.push(strs[0][startIndex]);
    startIndex++;
  }

  start.pop()

  return start.join("");
};