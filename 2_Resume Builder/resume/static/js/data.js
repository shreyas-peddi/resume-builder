function display(){

const name = document.getElementById('name').value;
const dob = document.getElementById('dob').value;
const email = document.getElementById('email').value;
const phone = document.getElementById('phone').value;
const address = document.getElementById('address').value;
const nationality = document.getElementById('nationality').value;
const domicile = document.getElementById('domicile').value;
const hometown = document.getElementById('hometown').value;

localStorage.setItem("Name",name);
localStorage.setItem("Dob",dob);
localStorage.setItem("email",email);
localStorage.setItem("phone",name);
localStorage.setItem("address",address);
localStorage.setItem("domicile",domicile);
localStorage.setItem("hometown",hometown);

return;
}

function data(){
	const Name = localStorage.getItem("Name");
	const Dob = localStorage.getItem("Dob");
	const Email = localStorage.getItem("email");
	const Phone = localStorage.getItem("phone");
	const Address = localStorage.getItem("address");
	const Domicile = localStorage.getItem("domicile");
	const Hometown = localStorage.getItem("hometown");

	document.getElementById('Name').innerHTML=Name;
	document.getElementById('Dob').innerHTML=Dob;
}