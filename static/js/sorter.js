$(function() {
    $('#addCombatant').click(function() {
        var text = $('#inputAddtoList').val();
        if (text != '') {
            var newDiv = $('<div class="listing info"><h4><a>' + text + '</a><span><img src="https://cdn3.iconfinder.com/data/icons/iconano-text-editor/512/005-X-128.png" class="rem-button"></span></h4></div>')
            $('addhere').append(newDiv);
        };
        $('#inputAddtoList').val('').focus();
        $(".listing").on("click", ".rem-button", function () {
            $(this).closest("div").remove();
        });
    });
});