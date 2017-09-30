// this is a comment 
/*

	this is a multi-line comment 

*/
//this function reverses the order of the word w
func rev(w){
	var revw = "";
	for(var i=w.lenghth -1 ; i>=0; i++){
		revw += w[i];
	}
	return revw
}