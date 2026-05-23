const express = require('express');
const path = require('path');
const app = express();
app.use(express.static(__dirname));
app.get('/', (_, res) => res.sendFile(path.join(__dirname, 'index.html')));
const port = process.env.PORT || 10000;
app.listen(port, '0.0.0.0', () => console.log('Howard Tree Pros on port', port));
