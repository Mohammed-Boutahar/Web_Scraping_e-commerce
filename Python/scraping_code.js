// Affichage dans la console:

// const scrape = require('./../index.js');
// const product = scrape('1005005218607714');

// product.then(res => {
//   console.log('The JSON: ', res);
// });


const csv = require('csvtojson');
const scrape = require('../JavaScript/aliexpress-product-scraper-master/src/aliexpressProductScraper.js');
const fs = require('fs');

process.setMaxListeners(40);


// // Store the CSV data in an array
// let csvData = [];
// csv()
//   .fromFile('product_keys.csv')
//   .then((data) => {
//     csvData = data;
//     // Loop through each object in the array
//       csvData.forEach((obj) => {
//         // Get the product key from the object
//         const productKey = obj['Product Keys'];
//         // Call the scrape function with the product key
//         const product = scrape(productKey);
//         product.then(res => {
//           //console.log('The JSON: ', res);
//           const jsonData = JSON.stringify(res);
//             // Écrire la chaîne de caractères dans un fichier
//           fs.writeFile(`data_${i}.json`,jsonData, 'utf8', (err) => {
//             if (err) {
//               console.error(err);
//               return;
//             }
//             console.log(`Le fichier data_${i}.json a été enregistré avec succès.`);
//             i++;
//           });
//         });
//       });
//   })
//   .catch((err) => {
//     console.error(err);
//   });

csvData=[]
fs.readFile('product_keys.csv', 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
    const idList = data.trim().split('\n');
    csvData = idList;
    csvData.shift();
  });

for(let j = 0; j<3; j++){
  const product = scrape(csvData[j]);
  product.then(res => {
    //console.log('The JSON: ', res);
    const jsonData = JSON.stringify(res);
    // Écrire la chaîne de caractères dans un fichier
    fs.writeFile(`data_${j+1}.json`,jsonData, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`Le fichier data_${j+1}.json a été enregistré avec succès.`);
    });
  });
}
  