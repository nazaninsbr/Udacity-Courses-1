let ageLimit = 21
var bouncerName = "Tony"

func deny(){
	print("Sorry but you can't go in")
}

func allow(){
	print("Welcome, enjoy your night")
}

func screenUnder21(age: Int, onGuestList: Bool){
	if(age>=ageLimit && onGuestList){
		allow()
	}
	else{
		deny()
	}
}

screenUnder21(age:17, onGuestList:true)
screenUnder21(age:17, onGuestList:false)
screenUnder21(age:27, onGuestList:true)
screenUnder21(age:27, onGuestList:false)