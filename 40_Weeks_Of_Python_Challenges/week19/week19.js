// # Date: 9/14/2023
// # Author: Shantel Williams

// # Problem: Create a function that takes a number num and returns its length.

// # Examples:
// # number_length(10) ➞ 2
// # number_length(5000) ➞ 4
// # number_length(0) ➞ 1

function number_length(num) {

    const str_num = num.toString();
    const array_num = str_num.split("");

    return array_num.length;

};

function main() {

    const tests = [number_length(10), number_length(5000), number_length(0)];

    let i = 0;

    while (i < tests.length) {
        console.log(tests[i]);
        i++;
    }
}

main()