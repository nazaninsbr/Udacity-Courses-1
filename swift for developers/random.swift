import Glibc

var nounArray = ["puppy", "laptop", "ocean", "app", "cow", "skateboard", "developer", "coffee", "moon"]


var index1 = Int(random()%9)
var index2 = Int(random()%9)
var sentence="The \(nounArray[index1]) is feeling \(nounArray[index2])"


print(sentence)