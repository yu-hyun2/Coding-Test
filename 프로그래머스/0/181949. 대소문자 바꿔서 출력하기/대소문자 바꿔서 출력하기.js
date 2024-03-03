const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    let str = input[0];
    let result = ""
    for (i = 0; i < str.length; i++){
        result += str[i] === str[i].toUpperCase() ? result[i] = str[i].toLowerCase() : result[i] = str[i].toUpperCase()
    }
    console.log(result)
});