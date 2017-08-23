$(document).ready(function() {
    // Materialize Navigator

    $(".button-collapse").sideNav('show');
    $(".button-collapse").sideNav({
        menuWidth: 250,
    });

    $('.collapsible').collapsible();

    $('.scrolly-link').scrollSpy({
        scrollOffset: 0,
    });

    //dropdownShow('.show-btn', '.section-container');
     $(document).ready(function(){
        $('.collapsible').collapsible();
     });
});

var dropdownShow = function(selectObject, targetObject) {
    $(selectObject).click(function () {
        $(targetObject).css('display', 'block');
    })
};