#!/usr/bin/node
const qu = require('./5-square.js');
class Square extends qu {
	constructor(size){
		super(size, size);

	}

	charPrint(c){
		let x,d;
        if(c === undefined){
			for(x=0;x < this.width;x++){
				let tmp = '';
				for(d=0;d < this.height;d++){
					tmp += 'X';
				}
				console.log(tmp);
		}
        }
		else{
		    for(x=0;x < this.width;x++){
				let tmp = '';
				for(d=0;d < this.height;d++){
					tmp += c;
				}
				console.log(tmp);
		}
		}
	}

}
module.exports = Square;
