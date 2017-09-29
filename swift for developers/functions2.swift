func sumOfStrings(_ aBunchOfStrings: [String])->Int{
	var sum=0
	for string in aBunchOfStrings{
		if string != nil{	
			let value: Int = Int(string)!
			sum += value
		}
	}
	return sum
}

print(sumOfStrings(["me", "see", "bee"]))