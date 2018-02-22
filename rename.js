var http = require('http');
var readline = require('readline-sync')
var util = require('util')
var colors = ['blue','powderblue','yellow','brown','orange','purple']

var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:powderblue;"><h1>This is my first header.</h1><p>Poort 8000</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8000)

var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:green;"><h1>This is my first header.</h1><p>Poort 8001</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8001)

var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:red;"><h1>This is my first header.</h1><p>Poort 8002</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8002)
var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:purple;"><h1>This is my first header.</h1><p>Poort 8003</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8003)
var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:pink;"><h1>This is my first header.</h1><p>Poort 8004</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8004)
var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:grey;"><h1>This is my first header.</h1><p>Poort 8005</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8005)
var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:white;"><h1>This is my first header.</h1><p>Poort 8006</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8006)
var server = http.createServer(function (req, res) {
    var html = '<!DOCTYPE html><html><body style="background-color:orange;"><h1>This is my first header.</h1><p>Poort 8007</p></body></html>'
    res.write(html); 
    res.end(); 
  }).listen(8007)

  
