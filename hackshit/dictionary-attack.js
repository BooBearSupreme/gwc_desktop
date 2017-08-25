var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;


/* ADD YOUR CODE BELOW */
//for loop
function checkPassword()
{
  var pws = document.getElementById("pw").value;
  for (i = 0; i < wordsList.length; i++)
  {
    if (wordsList[i] == pws)
    {
      alert("This password is BAAAAAAAAD. U SUCK.");
      return;
    }
  }
  //alert("This password is gucchi.");
  // var maxL= 20
  var minL=12

  if (pws.length <= minL){
    alert("This password is not the correct length.");
    return;
  }
  
  alert("This password is gucci.");
}
//any capital letters
