$('#chooseTicketFile').bind('change', function () {
  var filename = $("#chooseTicketFile").val();
  $("#noTicketFile").text(filename.replace("C:\\fakepath\\", "")); 
});

$('#chooseLicenseFile').bind('change', function () {
  var filename = $("#chooseLicenseFile").val();
  $("#noLicenseFile").text(filename.replace("C:\\fakepath\\", "")); 
});

$('#chooseDutFile').bind('change', function () {
  var filename = $("#chooseDutFile").val();
  $("#noDutFile").text(filename.replace("C:\\fakepath\\", "")); 
});