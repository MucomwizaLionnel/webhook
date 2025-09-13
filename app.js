// Import Express.js
const express = require('express');

// Create an Express app
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Set port and verify_token
const port = process.env.PORT || 3000;
const verifyToken = "EAAQcQV5uSMMBPTY0xRbfq0lYjJiffhG6qgvSGaPYWBY1FFo2vqqs3UyJKqgl98ezZBKTr8Di18yxpJPu70btrvuCJoSnwKhdsoL1xFJDSIx3ryBgrITI1WxCQUEveJaihgl6joeC2RxcL3NpMZApOyEYRe1DwmflXlwNcRACnl2ZACreAgVidnRJcLFYrgWvgkYheXo8nqdRSbc0qwPTfcuZAnZAYEYhe9UiiKm9GwQZDZD";

// Route for GET requests
app.get('/', (req, res) => {
  const { 'hub.mode': mode, 'hub.challenge': challenge, 'hub.verify_token': token } = req.query;

  if (mode === 'subscribe' && token === verifyToken) {
    console.log('WEBHOOK VERIFIED');
    res.status(200).send(challenge);
  } else {
    res.status(403).end();
  }
});

// Route for POST requests
app.post('/', (req, res) => {
  const timestamp = new Date().toISOString().replace('T', ' ').slice(0, 19);
  console.log(`\n\nWebhook received ${timestamp}\n`);
  console.log(JSON.stringify(req.body, null, 2));
  res.status(200).end();
});

// Start the server
app.listen(port, () => {
  console.log(`\nListening on port ${port}\n`);
});