/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let result = s;

  while (result.includes("()") || result.includes("[]") || result.includes("{}")) {
    nextResult = "";

    for (let i = 0; i < result.length; i++) {
      const pair = result[i] + result[i + 1];

      if (pair === "()" || pair === "[]" || pair === "{}") {
        i++;
        continue;
      }

      nextResult += result[i];
    }

    result = nextResult
  }

  return result === "";
};