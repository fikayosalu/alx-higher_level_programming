/* global $ */
$(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    if (!langCode) return; // Prevent API request if input is empty

    const url = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      console.error('Error: Failed to fetch translation.');
    });
  }

  // Click event for the Translate button
  $('#btn_translate').click(fetchTranslation);

  // Keypress event to allow ENTER key submission
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the ENTER key
      fetchTranslation();
    }
  });
});
