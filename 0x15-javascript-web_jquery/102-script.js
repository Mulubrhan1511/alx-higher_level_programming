$(document).ready(function() {
    $("input#btn_translate").click(function() {
      const languageCode = $("input#language_code").val();
      const apiUrl = `https://fourtonfish.com/hellosalut/?lang=${languageCode}`;
      $.get(apiUrl, function(data) {
        $("div#hello").text(data.hello);
      });
    });
  });