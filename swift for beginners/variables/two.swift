var numberOfServingsForRecipe = 10
var desiredNumberOfServings = 8

var servingsFactor = desiredNumberOfServings/numberOfServingsForRecipe 

// Calculate the number of pounds of tomatoes needed for 8 servings.
var poundsOfTomatoesForRecipe = 2
var amountToUseToday = poundsOfTomatoesForRecipe * servingsFactor

print(amountToUseToday)