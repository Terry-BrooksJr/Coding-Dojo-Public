
async function withAsync(num){
  // return new Promise((resolve,reject) => {
    if (num === 0){
      resolve('zero');
    } else {
      resolve('not zero');
    }
  }


withAsync(8)
    .then((resolveValue) => {
        console.log(` withAsync() returned a promise which resolved to: ${resolveValue}.`);
    });