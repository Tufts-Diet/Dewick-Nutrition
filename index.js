var express = require('express');
var app = express();
var path = require('path');
var PythonShell = require('python-shell');


const PORT=8000;

// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(PORT, function(){
    //Callback triggered when server is successfully listening. Hurray!
    console.log("Server listening on: http://localhost:%s", PORT);
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