/*
 * Programming Quiz: Inline Functions (5-6)
 */

// don't change this code
function emotions(myString, myFunc) {
    console.log("I am " + myString + ", " + myFunc(2));
}

// your code goes here
// call the emotions function here and pass in an
// inline function expression
function laugh(num){
    var ans = "";
    for(var i=0; i<num; i++){
        ans = ans + "ha";
    }
    ans = ans + "!";
    return ans;
}
emotions("happy", laugh);