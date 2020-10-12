//Udemy: JavaScript Algorithms and Data Structures Masterclass
//Problem Solving Patters/Approach
// #1 - Understand The Pproblem
// #2 - Concrete Examples
// #3 - Break It Down
// #4 - Solve and Simplify
// #5 - Look Back & REfactor


//Frequency Counters
    // This pattern uses objects or sets to collect values/frequencies of values
    // This can often avoid the need for nested loops or O(n^2) operations with arrays/strings

// Write a function called same, which accepts two arrays.
// The function should return true if every value in the array has it's corresponding value squared in the second array.
// The frequency of values must be the same.

//Naive Solution o(n^2)
function same(array1, array2){

    if(array1.length !== array2.length){
        return false;
    }
    for(let i = 0; i < array1.length;i++){
        let correctIndex = array2.indexOf(array1[i] ** 2)
        if(correctIndex === -1){
            return false;
        }
        array2.splice(correctIndex,1);
    }
    return true;
}

console.log(same([1,3,2],[4,1,9]));
console.log('------------------------')

function same2(array1, array2){
    if(array1.length !== array2.length){
        return false;
    }
    let frequencyCounter1 = {}
    let frequencyCounter2 = {}
    for (let val of array1){
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) +1
    }
    for(let val of array2){
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) +1
    }
    for(let key in frequencyCounter1){
        if(!(key**2 in frequencyCounter2)){
            return false;
        }
        if(frequencyCounter2[key ** 2] !== frequencyCounter1[key]){
            return false;
        }
    }
    console.log(frequencyCounter1);
    console.log(frequencyCounter2);
    return true;
}

console.log(same2([1,3,2,2,2],[4,1,4,4,9]));

console.log('--------------------------------')


// Given two streings, write a function to determine if the second string is an anagram of the first.
// An anagram is a word, phrase, or name formed by rearranging the letters of another,  such as cinema, formed from iceman.

function validAnagram(string1, string2){
    // compare length of strings return false if not equal
    console.log('Step 1:')
    if(string1.length !== string2.length){
        console.log(string1)
        return false;
    }
    console.log('Step 2:')
    // make my frequency counter objects
    let frequencyCounter1 = {}
    let frequencyCounter2 = {}

    // loop thru the string characters
    // if a letter is in the counter already add 1 if not set it to 1
    console.log('Step 3:')
    for(let val of string1){
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1;
    }
    for(let val of string2){
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) +1;
    }
    console.log(frequencyCounter1);
    console.log(frequencyCounter2);
    // compare that the frequency counter objects are the same
    if(frequencyCounter1 !== frequencyCounter2){
        return false;
    }
    // return true if it is false if it isn't
    console.log('Step 4:')

    return true;

}
console.log(validAnagram('catttt', 'tatttc'));