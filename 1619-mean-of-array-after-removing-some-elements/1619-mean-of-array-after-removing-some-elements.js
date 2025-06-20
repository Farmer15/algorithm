/**
 * @param {number[]} arr
 * @return {number}
 */
var trimMean = function(arr) {
    const sortedArr = arr.slice().sort((a, b) => a - b);
    const cut = Math.floor(arr.length * 0.05); 
    let count = 0;
    
    const filteredSum = sortedArr.reduce((acc, num, i) => {
        if (i >= cut && i < arr.length - cut) {
            count++;
            return acc + num;
        }
        return acc;
    }, 0);

    return filteredSum / count;
};