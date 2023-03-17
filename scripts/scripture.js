//---upon opening, a random scripture is displayed:

//declare a global empty array:
var scriptureList = ""
//set the variable for the button
let randomButton = document.querySelector("#newRandom")

//Declare a function named outputScripture that accepts a reference and verse
function outputScripture(referenceString, verse) {
  let referenceElement = document.querySelector("#reference")
  referenceElement.innerHTML = referenceString

  let scriptureElement = document.querySelector("#scripture")
  scriptureElement.innerHTML = verse
}

//pulling a random number to find the verse to display:
function getRandomNumber() {
  // 41996 is the amount of verses in the bible and in the lds-scriptures
  //the following came from: https://stackoverflow.com/questions/1527803/generating-random-whole-numbers-in-javascript-in-a-specific-range
  let number = Math.floor(Math.random() * (41996 - 1) + 1)
  return number
}

//get the URL depending on what the randomNumber is.
function getUrl(number) {
  //31102 is how many verses are in the bible.
  if (number > 31102) {
    //so if it's greater than that, use the lds-scriptures
    url =
      "https://raw.githubusercontent.com/jlassig/cse121b/main/lds-scriptures.json"
  } else {
    //otherwise, just use the bible
    url = "https://raw.githubusercontent.com/jlassig/cse121b/main/bible.json"
  }
  return url
}

//fetch from API the scripture's info:
async function getScriptureInfo() {
  let randomNumber = getRandomNumber()
  let url = getUrl(randomNumber)
  if (randomNumber > 31102) {
    //since we added the bible and LDS verses together, we need to get the number and change it here if it is larger than the number of verses in the bible.
    randomNumber = randomNumber - 31102
  }
  const response = await fetch(url)
  //if that's all done:
  if (response.ok) {
    //put the info into a list
    scriptureList = await response.json()
  }
  //iterate through that list and find the scripture entry that we want to display.
  let aScripture = scriptureList[randomNumber]
  //now get the reference and the scripture text
  let theReference = aScripture["verse_title"]
  let theScripture = aScripture["scripture_text"]
  outputScripture(theReference, theScripture)
}

//----user clicks a button and the screen is cleared and a new random scripture is displayed:
randomButton.addEventListener("click", getScriptureInfo)

getScriptureInfo()
