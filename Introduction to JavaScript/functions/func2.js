/*
 * Programming Quiz: Laugh it Off 2 (5-2)
 */
 
// declare your function
// then, call it!
// print the output with console.log
function laugh(num){
    var ans = "";
    for(var i=0; i<num; i++){
        ans = ans + "ha";
    }
    ans = ans + "!";
    return ans;
}
console.log(laugh(3));
