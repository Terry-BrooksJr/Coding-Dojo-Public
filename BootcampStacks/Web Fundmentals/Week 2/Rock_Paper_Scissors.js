// const getUserChoice = function(userInput) {
//   userInput = userInput.toLowerCase();
//   if (userInput === 'rock'||userInput==='paper'||userInput==='scissors'){
//     return userInput
//   } else {
//     console.log('You Have Selected an Invaild Option')
//   }
// }
// function getComputerChoice(){
//   choice=Math.floor(Math.random()*3)
//   if (choice===0){
//     return 'rock'
//   }
//   else if (choice===1){
//     return 'paper'
//   } else if (choice ===2){
//     return 'scissors'
//   }
//   }
function determineWinner(userChoice, computerChoice) {
  if (userChoice === computerChoice) {return 'Tie Game!'};
  if (userChoice === 'rock' && computerChoice === 'paper') {return 'The Computer Won!';} else { return 'You Won!'; };
  if (userChoice === 'paper' && computerChoice === 'scissors') {return 'The Computer Won!';} else { return 'You Won!'; };
  if (userChoice === 'scissors' && computerChoice === 'rock') {return 'The Computer Won!';} else { return 'You Won!'; };
}
console.log('Test 1')
const userChoice1 = 'paper';
const computerChoice1 = 'scissors';
console.log(determineWinner(userChoice1, computerChoice1));  console.log('This Should log the Computer Wins')//;Computer Wins
console.log("=====================")
console.log('Test 2')
const userChoice2 = 'rock';
const computerChoice2 = 'scissors';
console.log(determineWinner(userChoice2, computerChoice2)); console.log('This should log You WIn') //You Wins
console.log("=====================")
console.log('Test 3')
const userChoice3 = 'scissors';
const computerChoice3= 'scissors';
console.log(determineWinner(userChoice3, computerChoice3)); console.log('This should log a tie') //tie game
