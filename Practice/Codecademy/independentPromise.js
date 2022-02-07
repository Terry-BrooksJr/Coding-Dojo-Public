import { cookBeans, steamBroccoli, cookRice, bakeChicken } from 'Practice/Codecademy/independentPromiseLibrary.js';

// Write your code below:
async function serveDinner() {
    const vegetablePromise = steamBroccoli();
    const starchPromise = cookRice();
    const proteinPromise = bakeChicken();
    const sidePromise = cookBeans();
    return `Dinner is served. We’re having ${await vegetablePromise}, ${await starchPromise}, ${await proteinPromise}, and ${await sidePromise}.`;
}
console.log(serveDinner());