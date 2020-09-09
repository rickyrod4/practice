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
}


