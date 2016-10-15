var express = require('express');
var app = express();
var path = require('path');
var PythonShell = require('python-shell');
var jsonfile = require('jsonfile');

var allowCrossDomain = function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With');

    // intercept OPTIONS method
    if ('OPTIONS' == req.method) {
      res.sendStatus(200);
    }
    else {
    	next();
    }
};

	app.use(allowCrossDomain);
	app.use(express.static(__dirname + '/public'));

app.set('port', (process.env.PORT || 8000));

var py_options = {
scriptPath: __dirname + '/'
};

PythonShell.run('simple_test.py', py_options, function (err, results) { 
//your code (sets variables for files?)
});

// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/FoodInfo.json', function(req,res) {

  var file = __dirname + '/FoodInfo.json';

  jsonfile.readFile(file, function(err, obj) {
    if(err) {
      res.json({status: 'error', reason: err.toString()});
      return;
    }
    res.send(JSON.stringify((obj)));
  });
});

app.listen(app.get('port'), function(){
    //Callback triggered when server is successfully listening. Hurray!
    console.log("Server listening on: http://localhost:%s", app.get('port'));
});
