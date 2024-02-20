var input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
let b = parseInt(input[1]);

let arr = [];
let aCopy = a;
let numVal = 1;

while (aCopy != 1) {
    if (aCopy % 2 == 1) {
        arr.unshift(numVal);
        aCopy -= 1;
    }
    aCopy = aCopy / 2;
    numVal = numVal * 2;
}
arr.unshift(numVal);

let bCopy = b;
let bVal = 0;
while (bCopy != arr.length) {
    bVal += arr[bCopy];
    bCopy++;
}
console.log(arr[b - 1] - bVal);
