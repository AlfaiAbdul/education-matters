
function getDependentValues(){
    var satAvg = d3.select("#satAvg").node().value;
    var tutionFee = d3.select("#tutionFee").node().value;
    var age = d3.select("#age").node().value;
    var hhIncome = d3.select("#hhIncome").node().value;
//var stuIncome = d3.select("#income").node().value;

    console.log("satAvg : ", satAvg);
    console.log("tutionFee : ", tutionFee);
    console.log("age : ", age);
    console.log("hhIncome : ", hhIncome);

    url = "/prediction/"+satAvg+"/"+tutionFee+"/"+age+"/"+hhIncome
	var stuIncome = "";
    d3.json(url, function (error, response) {
			console.log("Inside API")
            console.log(response);

            var data = response
            stuIncome = response;
    });  
	
	document.getElementById("income").innerHTML = stuIncome;	
}





