import Foundation 


func firstLetterLast(_ word:String)-> String{
	var word = word
	word.append(word[word.startIndex])
	word.remove(at:word.startIndex)
	return word
}

print(firstLetterLast("helloYou"))