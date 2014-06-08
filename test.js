/* global console:true */
/* global FOO */

var unused = {
  foo:5,
  foo: 5,
  single: 'single quote',
  no_camel: 5,
  default: 3,
  doubleQuote: "double quote",
  extracomma: 5,
},
  no_camel, key, key, obj = {}, dump = lateDefVar, lateDefVar;

function unusedfunc() {}

lateDefFunc();
function lateDefFunc() {}

//no semi colon
dump = 5
dump = arguments.callee;
notDefined = 5;
//this line is too long ---------------------------------------------------------
  return; //wrong indentation

Array.prototype.count = undefined; //don't extend native objects
//not wrapping immediately executed function in parenthesis
dump = function () {}();

//no strict, double declaration
(function tooManyParams(arg1, arg2) {
  var doubleDeclaration, doubleDeclaration;
  return arg1 && arg2 && doubleDeclaration; //silence unused
})();

// too deep nesting
if (true) {
  if (true) {
    if (true) {
      return;
    }
  }
}

if (5 == 4 && 5 == 3 && 4 != 5) {
  dump++; //unexpected use of --/++
  dump--;
  dump = 5+2; //missing whitespace
}

function tooManyVar() {
  'use strict';
  var foo;


  for (var key in obj) { // too many var statement and the body of a for in statement should be wrappen in a if (Object.hasOwnProperty.. etc)
    return;
  }

  with (window) { return; } //with is not allowed
  return foo && key;
}

with (window) { return; } //with is bad

if (true) return; //require curly

if (true)
  return; //same as above, but newline
