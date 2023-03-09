//Import des scripts necessaires et bibliothèques pour faire le scraping
const scrape = require('../JavaScript/aliexpress-product-scraper-master/src/aliexpressProductScraper.js');
const fs = require('fs');

// Modification du nombre de Listeners pour augmenter la capacité de la machine
process.setMaxListeners(40);


// Cette petite partie permet de lire le CSV des cles des produits et les afficehr en cas de besoin  
csvData=[]
fs.readFile('product_keys.csv', 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
    const idList = data.trim().split('\n');
    csvData = idList;
    csvData.shift();
    // csvData.forEach(element => {
    //   console.log(element);
    // });
  });

//-_-_-_IMPORTANT-_-_-_//
// Il s'est avéré qu'il est quasiment impossible de boucler les cles des produits 
//sur le code suivant car nous rencontrons des erreurs de mémoire et du système
//Ce code nécessite un serveur vue le potentiel de scraper ces données sans clé API ni accès direct aux feedback des clients


// "i" prend la cle du produit
const i = "1005005046954479";
const product = scrape(i);
product.then(res => {
  const jsonData = JSON.stringify(res);
  // Écrire la chaîne de caractères dans un fichier
  fs.writeFile(`data_${i}.json`,jsonData, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`Le fichier data_${i}.json a été enregistré avec succès.`);
  });
});



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