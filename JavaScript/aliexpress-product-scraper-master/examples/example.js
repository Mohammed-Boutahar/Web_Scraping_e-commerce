// Affichage dans la console:

// const scrape = require('./../index.js');
// const product = scrape('1005005218607714');

// product.then(res => {
//   console.log('The JSON: ', res);
// });




const csv = require('csvtojson');
const scrape = require('./../src/aliexpressProductScraper.js');
const fs = require('fs');

// Store the CSV data in an array
let csvData = [];
csv()
  .fromFile('product_keys.csv')
  .then((data) => {
    csvData = data;

    //ERROR HERE, THE CSV FILE IS NOT READ PROPERLY, IT SHOWS 1 INSTEAD THE PRODUCT KEY
    
     // Loop through each object in the array
     csvData.forEach((obj) => {
      // Get the product key from the object
      const productKey = obj['Product Keys'];

      // Call the scrape function with the product key
      const product = scrape(productKey);
      product.then(res => {
        //console.log('The JSON: ', res);
        const jsonData = JSON.stringify(res);

        // Écrire la chaîne de caractères dans un fichier
        fs.writeFile(`data_${productKey}.json`,jsonData, 'utf8', (err) => {
          if (err) {
            console.error(err);
            return;
          }
          console.log(`Le fichier data_${productKey}.json a été enregistré avec succès.`);
        });
      });
    });
  });



