var express = require('express');
var app = express();
var path = require('path');
var PythonShell = require('python-shell');

app.set('port', (process.env.PORT || 8000));

var py_options = {
scriptPath: '~/Desktop/Just\ for\ me/Dewick-Nutrition/'
};

PythonShell.run('data_mine.py', py_options, function (err, results) { 
//your code (sets variables for files?)
});

// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.get('/BreakfastLowCal', function(req,res) {

});

app.get('/BreakfastMedCal', function(req,res) {

});

app.get('/BreakfastHighCal', function(req,res) {

});

app.get('/LunchLowCal', function(req,res) {
	
});

app.get('/LunchMedCal', function(req,res) {
	
});

app.get('/LunchHighCal', function(req,res) {
	
});

app.get('/DinnerLowCal', function(req,res) {
	
});

app.get('/DinnerMedCal', function(req,res) {
	
});

app.get('/DinnerHighCal', function(req,res) {
	
});

app.get('/Meals', function(req,res) {
	
});

app.listen(app.get('port'), function(){
    //Callback triggered when server is successfully listening. Hurray!
    console.log("Server listening on: http://localhost:%s", app.get('port'));
});
