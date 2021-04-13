/* This function is called when the submit button is pressed/
 *
 * See the "on" attribute of the submit button */
function process(){
  console.log('hi');

  // we have really long feature names =(
  feature = {
    'petal length (cm)': $('#petal_length').val(),
    'petal width (cm)':  $('#petal_width').val(),
    'sepal length (cm)': $('#sepal_length').val(),
    'sepal width (cm)':  $('#sepal_width').val()
  }

  // Call our API route /predict_api via the post method
  // Our method returns a dictionary.
  // If successful, pass the dictionary to the function "metis_success"
  // If there is an error, pass the dictionary to the functoin "metis_error"
  // Note: functions can have any name you want; to demonstrate this we put
  //       metis_ at the beginning of each function.
  $.post({
    url: '/search_api',
    contentType: 'application/json',
    data: JSON.stringify(feature),
    success: result => metis_success(result),
    error: result => metis_error(result)
  })
}

function ourRound(val, decimalPlaces=1){
  // Javascript rounds to integers by default, so this is a hack
  // to round to a certain number of decimalPlaces
  const factor = Math.pow(10, decimalPlaces)
  return Math.round(factor*val)/factor
}

/* Here "result" is the "dictionary" (javascript object)
 * that our get_api_response function returned when we called
 * the /predict_api function
 *
 * Here we select the "results" div and overwrite it
 */
function metis_success(result){
  $('#results').html(`The most likely class is ${result.most_likely_class_name}
                      with probability ${ourRound(100*result.most_likely_class_prob)}%`);

  const all_results = result.all_probs.map( (data) => `${data.name}: ${ourRound(100*data.prob)}`)
  $('#list_results').html(all_results.join('%<br>') + '%');

  // only included in predictor_javascript_slider_graph.html
  // otherwise does nothing.
  modifyDivs(result.all_probs);
}

function metis_error(result){
  console.log(result);
  alert("I don't know what you did");
}

$(function() {
  $('input[type=file]').change(function(){
    var t = $(this).val();
    var labelText = 'File : ' + t.substr(12, t.length);
    $(this).prev('label').text(labelText);
  })
});