let nums = [1, 2, 3, 4, 5, 6];
let array = new Array();

function last(index) {
    return nums[index]
}

function second(index) {
    let num = last(index);
    if (num % 2 == 0) {
        array.push(num)
    }
}

function first(index) {
    second(index)
}

for (let i = 0; i < nums.length; i++) {
    first(i)
}

console.log(array)