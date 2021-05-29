
// var nums = [1, 2, 3, 4];

// for (var i = 1; i < nums.length; i++){
//     nums[i] += nums[i - 1];
// }
// console.log(nums);

// var nums = [1, 2, 3, 4];
// var sma = nums[0]
// for (var i = 0; i < nums.length; i++){
//     if (nums[i] < sma) {
//         sma = nums[i]
//     }
// }
// console.log(sma);




var nums = 'aman';
for (var i = 0; i < nums.length; i++) {
    var sma = ""
    for (var j = i ; j < nums.length; j++) {
        sma += nums[j]
        console.log(sma);
    }
}









var arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 6],
    [7, 8, 9, 9],
    [2, 4, 1, 3]
];

var row = arr.length;
var col = arr[0].length

var firstDiago = 0;
var secondDiago = 0;

for (var i = 0; i < row; i++) {
    firstDiago += (arr[i][(row - i) - 1]);
    for (var j = 0; j < col; j++) {
        if (i == j) {
            secondDiago += (arr[i][j]);
        }
    }
}

var diff = secondDiago - firstDiago;
console.log(Math.abs(diff));