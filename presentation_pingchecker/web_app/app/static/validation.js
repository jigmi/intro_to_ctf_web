function ValidateIPaddress(inputText)
 {
 var ipformat = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
 if(inputText.value.match(ipformat))
 {
 document.ip_form.ip.focus();
 return true;
 }
 else
 {
 var div = document.getElementById("output");
 var message = "<p>Invalid format for IP address, try harder</p>";
 div.innerHTML = message;
 document.ip_form.ip.focus();return false;
 }
 }