const { checkAvailability } = require('/Users/terrybrooksjr/Documents/GitHub/Coding-Dojo-Public/Upskilling Practice/Codecademy/promisesLibrary2.js');

const onFulfill = (itemsArray) => {
    console.log(`Items checked: ${itemsArray}`);
    console.log(`Every item was available from the distributor. Placing order now.`);
};

const onReject = (rejectionReason) => {
    console.log(rejectionReason);
};

// Write your code below:

const checkSunglasses = checkAvailability('sunglasses', 'Favorite Supply Co.');

const checkPants = checkAvailability('pants', 'Favorite Supply Co.');

const checkBags = checkAvailability('bags', 'Favorite Supply Co.');

const allPromises = [checkAvailability, checkPants, checkSunglasses];
var myPromises = Promise.all(allPromises)
                    .then(onFulfill)
                    .catch(onReject);

// Promise.all([checkSunglasses, checkPants, checkBags])
//     .then(onFulfill)
//     .catch(onReject);


// let endResult = (myPromises.then(onFulfill) (myPromises.catch(onReject)));
