//Practice

//Write a function that returns the largest element in an array.
console.log('Largest')
function largest(arr){
    console.log(arr);
    var max = arr[0];
    for(var i = 0; i<arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}
 
console.log(largest([0,2,14,6,8]));


console.log('--------------------------------------');


console.log('Singly Linked List');

class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}
my_node = new Node(10);


class SLL{
    constructor(){
        this.head = null;
    }

    view(my_node){
        var currentNode = this.head;
        while(currentNode){
            console.log('Current node is: ${currentNode.value}');
            currentNode = currentNode.next;
        }
    }
    }

//view(my_node);

console.log('--------------------------------')
//To Do 1
//Push Front
//Given an array and an additional value, insert this value at the beginning of the array. 
//Do this without using any built-in array methods.
console.log('Push Front');
function pushFront(arr, val){
    console.log(arr + ', New value to push: ' + val);
    for(var i = arr.length; i>0; i--){
        arr[i] = arr[i-1];

    }
    arr[0] = val;
    console.log(arr)
}

pushFront([0,2,4,6,8,10], 5)
console.log('----------------------------------');


console.log('Pop Front')
//Pop Front
//Given an array, remove and return the value at the beginning of the array. 
//Do this without using any built-in array methods except pop().
function popFront(arr){
    console.log(arr)
    var first_value = arr[0];
    var temp;
    for(var i = 0; i < arr.length-1;i++){
        temp = arr[i];
        arr[i]=arr[i+1];
        arr[i+1]=temp;
    }
    arr.pop();
    console.log('New Array:', arr);
    return first_value;
}

console.log(popFront([1,2,3,4,5]))


console.log('----------------------------------');


console.log('Insert At')
//Insert At
//Given an array, index, and additional value, insert the value into array at given index. 
//Do this without using built-in array methods. 
//You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val).

function insertAt(arr, index, val){
    console.log(arr, '- Insert:', val, '@ index:',index);
    for(var i = arr.length; i > index; i--){
        arr[i] = arr[i-1];
    }
    arr[index] = val;
    console.log('New Array: ', arr);
    return arr;

}

insertAt([2,4,6,8,10], 2, 'Hello');




console.log('----------------------------------');



console.log('Min To Front')
//Min to Front
//Given an array of comparable values, move the lowest element to array’s front, shifting backward any elements previously ahead of it. 
//Do not otherwise change the array’s order. Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. 
//As always, do this without using built-in functions.

function minToFront(arr){
    console.log(arr)
    //iterate thru the array
    var min = arr[arr.length-1];
 

    for(var i = arr.length-1; i > 0; i--){
        //find the min value
        if(arr[i]<min){
            min = arr[i];
            var index = i;
        }
        //compare values move lower value to the left
    }
    var temp;
    for(var i = index; i > 0; i--){
        if(arr[i] < arr[i-1]){
            //move the lowest value all the way to the left
            temp = arr[i-1];
            arr[i-1]=arr[i];
            arr[i] = temp;
        }
    }
    console.log(min);
    console.log(arr);
    console.log(index)
    return arr;

}
minToFront([5,20,10,2,17,6]);
console.log('------------------------------------')


function max(array){
    var maximum = array[0];
    for(var i = 0; i<array.length;i++){
        if(array[i]>maximum){
            maximum = array[i];
        }
    }
    return maximum;
}

console.log(max([0,3,4,5,1]))


console.log('------------------------------')
console.log('Add Up To n Function')
function addUpTo(n){
    var total = 0;
    for(var i = 0;i <= n; i++){
        total += i;
    }
    return total;
}

console.log(addUpTo(6));

