/*
 * Programming Quiz: Laugh (5-4)
 */

var laugh = function (num){
    var ans = "";
    for(var i=0; i<num; i++){
        ans = ans + "ha";
    }
    ans = ans + "!";
    return ans;
}

console.log(laugh(10));