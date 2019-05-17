$(function () {

    function q(selector) { return document.querySelector(selector)}

    $( '#poem' ).addClass( 'poemtype' );
    $( '#한국어' ).addClass( 'kortext' );
    $( '#영어' ).addClass( 'engtext' );

    $('.audiostore-item').click(function () {
        // alert("ajax 코드");
        $.ajax({
            url: '/tts/audioStore/',
            dataType: 'json',
            data: { 'id': $(this).attr("id") },
            success: function (result) {
                result = JSON.parse(result)
                title = result['fields']['title']
                author = result['fields']['author']
                contents = "/media/" + result['fields']['contents']
                audio = "/media/" + result['fields']['audio']
                var url = contents
                $.get(url, function(str){
                    var results = str.split("\n");
                    var results2="";
                    $.each(results, function(index, element){
                      results2 += element + "<br>";
                    });
                    $('.content-text').html(results2);
                });
                $('.content-title').text(title)
                $('.content-author').text(author)
                q('#content-audio').hidden = false;
                q('#content-audio').src = audio
            }
        });
    });

    $('.close-button').click(function () {

        $('audio').each(function(){
            this.pause(); // Stop playing
            this.currentTime = 0; // Reset time
        }); 

    });

    $('.rounded-pill').click(function () {

        $('audio').each(function(){
            this.pause(); // Stop playing
            this.currentTime = 0; // Reset time
        }); 

    });
});
