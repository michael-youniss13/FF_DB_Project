function transform(data) {
  // filter functions are passed the whole API response object
  // you may manipulate or add to this data as you want

  // query parameters exist in the global scope, for example:
  // http://www.kimonolabs.com/apis/<API_ID>/?apikey=<API_KEY>&myparam=test
  // query.myparam == 'test';  // true
  
  var results = [];
  var arr = data.results.collection1;
  for (var res in arr) {
    
    var name = arr[res].name;
    var receivingYards = arr[res].receivingYards;
    var receivingTds = arr[res].receivingTDs;
    var receptions = arr[res].receptions;
    var rushingYards = arr[res].rushingYards;
    var rushingTds = arr[res].rushingTDs;
    
    var proj = 0.0;
    proj += (receptions*1.0);
    proj += (receivingYards/10.0);
    proj += (receivingTds*6.0);
    proj += (rushingYards/10.0);
    proj += (rushingTds*6.0);
    if(receivingYards > 100){
      proj += 3.0;
    } 
    if(rushingYards > 100){
      proj += 3.0;
    }

    proj = proj * 100;
    proj = Math.round(proj);
    proj = proj / 100;
    results.push([name, proj]);
    
  }

  return results;
}