
function getDependentValues(){
    var satAvg = d3.select("#satAvg").node().value;
    var tutionFee = d3.select("#tutionFee").node().value;
    var age = d3.select("#age").node().value;
    var hhIncome = d3.select("#hhIncome").node().value;
    console.log("satAvg : ", satAvg);
    console.log("tutionFee : ", tutionFee);
    console.log("age : ", age);
    console.log("hhIncome : ", hhIncome);

    url = "/prediction/"+satAvg+"/"+tutionFee+"/"+age+"/"+hhIncome
    d3.json(url, function (error, response) {
        
            console.log(response);

            var data = response
            years = response;
            

    });  
}





