/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let i = num1.length - 1, j = num2.length - 1;
    let carry = 0;
    let result = [];

    while (i >= 0 || j >= 0 || carry) {
        let digit1 = i >= 0 ? num1.charAt(i) - '0' : 0;
        let digit2 = j >= 0 ? num2.charAt(j) - '0' : 0;

        let total = digit1 + digit2 + carry;
        carry = Math.floor(total / 10);

        result.push(total % 10);

        i--;
        j--;
    }

    return result.reverse().join('');
};