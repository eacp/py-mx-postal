// A function to request something based on its cp

const postalURI = (code) => `/cp/${code}.json`;


// Get the DOM elements

const postal = document.getElementById("cp");
const city = document.getElementById("city");
const munip = document.getElementById("muni");
const state = document.getElementById("state");
const area = document.getElementById("area");


const fill = (data) => {
	console.log(data);

	// Fill fields
	city.value = data.ciudad;
	munip.value = data.municipio;
	state.value = data.estado;

	// Add options

	// Reset the dropdown
	area.innerHTML = '';

	data.areas.forEach(a => {
		let opt = document.createElement("option");
		opt.value = a.name;
		opt.innerHTML = a.name;

		area.append(opt);
	});


}


// Make a cache
let cache = {};

function fetchPostal(code) {
	if(code.length != 5) {
		console.log("Invalid:",code, code.length);
		return;
	}

	if(code in cache) fill(cache[code]);

	// Make the request
	fetch(postalURI(code)).then(response => response.json())
	.then((data) => {
		// Fill
		fill(data);
		cache[code] = data;
	});
}