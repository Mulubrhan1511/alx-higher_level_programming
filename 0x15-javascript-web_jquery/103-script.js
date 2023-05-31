$(document).ready(function() {
    function fetchTranslation(languageCode) {
      const apiUrl = `https://fourtonfish.com/hellosalut/?lang=${languageCode}`;
      $.get(apiUrl, function(data) {
        $("div#hello").text(data.hello);
      });
    }
  
    $("input#btn_translate").click(function() {
      const languageCode = $("input#language_code").val();
      fetchTranslation(languageCode);
    });
  
    $("input#language_code").keypress(function(event) {
      const keyCode = event.keyCode || event.which;
      if (keyCode === 13) {
        const languageCode = $("input#language_code").val();
        fetchTranslation(languageCode);
      }
    });
  });