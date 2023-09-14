#!/usr/bin/node
const SQ = require('./5-square.js');
class Square extends SQ{
	constructor(size){
		super(size,size)

	}

	charPrint(c){
		let x,d;
        if(c === undefined){
			for(x=0;x < 4;x++){
				let tmp = '';
				for(d=0;d < 4;d++){
					tmp += 'X';
				}
				console.log(tmp);
		}
        }
		else{
		    for(x=0;x < 4;x++){
				let tmp = '';
				for(d=0;d < 4;d++){
					tmp += c;
				}
				console.log(tmp);
		}
		}
	}

}
