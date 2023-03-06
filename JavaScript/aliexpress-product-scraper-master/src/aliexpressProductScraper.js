const puppeteer = require('puppeteer');
const cheerio = require('cheerio');

const Feedback = require('./feedback');

async function AliexpressProductScraper(productId, feedbackLimit) {
  const FEEDBACK_LIMIT = feedbackLimit || 10;
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  /** Scrape the aliexpress product page for details */
  await page.goto(`https://www.aliexpress.com/item/${productId}.html`);
  const aliExpressData = await page.evaluate(() => runParams);
  
  const data = aliExpressData.data;

  /** Scrape the description page for the product using the description url */
  const descriptionUrl = data.descriptionModule.descriptionUrl;
  await page.goto(descriptionUrl);
  const descriptionPageHtml = await page.content();

  /** Build the AST for the description page html content using cheerio */
  const $ = cheerio.load(descriptionPageHtml);
  const descriptionData = $('body').html();

  /** Fetch the adminAccountId required to fetch the feedbacks */
  const adminAccountId = await page.evaluate(() => adminAccountId);
  await browser.close();

  let feedbackData = [];

  if (data.titleModule.feedbackRating.totalValidNum > 0) {
    feedbackData = await Feedback.get(
      data.actionModule.productId,
      adminAccountId,
      data.titleModule.feedbackRating.totalValidNum,
      FEEDBACK_LIMIT
    );
  }

  /** Build the JSON response with aliexpress product details */
  const json = {
    feedback: feedbackData,
  };

  return json;
}

module.exports = AliexpressProductScraper;
