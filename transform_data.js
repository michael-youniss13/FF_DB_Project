function transform(data) {
  // filter functions are passed the whole API response object
  // you may manipulate or add to this data as you want

  // query parameters exist in the global scope, for example:
  // http://www.kimonolabs.com/apis/<API_ID>/?apikey=<API_KEY>&myparam=test
  // query.myparam == 'test';  // true
  
  var results = [];
  var arr = data.results.collection1;
  for (var res in arr) {
    
    var name = arr[res].name.text;
    var passingYards = arr[res].passingYards;
    var passingTds = arr[res].passingTDs;
    var interceptions = arr[res].passingINTs;
    var rushingYards = arr[res].rushingYards;
    var rushingTds = arr[res].rushingTDs;
    
    var proj = 0.0;
    proj += (passingYards/25.0);
    proj += (passingTds*4.0);
    proj -= interceptions;
    proj += (rushingYards/10.0);
    proj += (rushingTds*6.0);
    if(passingYards > 300){
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