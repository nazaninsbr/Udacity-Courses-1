/*
 * Programming Quiz: Countdown, Liftoff! (4-3)
 * 
 * Using a while loop, print out the countdown output above.
 */

var t = 60; 
while(t>=0){
    if(t>0 && (t%10!==0 || t===60)){
        console.log("T-"+t+" seconds")
    }else if(t%10===0 && t!==0){
        console.log("Orbiter transfers from ground to internal power")
    }else{
        console.log("Solid rocket booster ignition and liftoff!")
    }
    t = t-1;
}