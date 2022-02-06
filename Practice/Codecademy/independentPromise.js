import { cookBeans, steamBroccoli, cookRice, bakeChicken } from 'Practice / Codecademy / independentPromiseLibrary.js';

// Write your code below:
async function serveDinner() {
    const vegetablePromise = steamBroccoli();
    const starchPromise = cookRice();
    const proteinPromise = bakeChicken();
    const sidePromise = cookBeans();
}