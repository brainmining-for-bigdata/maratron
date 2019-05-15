$(function () {

    function q(selector) { return document.querySelector(selector)}

    $('.audiostore-item').click(function () {
        // alert("ajax 코드");

        $.ajax({
            url: '/tts/audioStore/',
            dataType: 'json',
            data: { 'href': $(this).attr("href") },
            success: function (result) {
                result = JSON.parse(result)
                // console.log(result)

                title = result['fields']['title']
                author = result['fields']['author']
                contents = "/media/" + result['fields']['contents']
                audio = "/media/" + result['fields']['audio']
                console.log(audio)
                console.log(typeof(audio))
                var url = contents
                $.get(url, function(str){
                    var results = str.split("\n");
                    var results2="";
                    $.each(results, function(index, element){
                    //   console.log(element);
                      results2 += element + "<br>";
                    });
                    $('.content-text').html(results2);
                });
                // console.log("result는 ", audio)
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
