$(document).ready(function() {
    // Materialize Navigator
    //$(".button-collapse").sideNav('show')
    $(".button-collapse").sideNav({
        menuWidth: 260,
        //edge: 'right'
    });
    // Homepage Parallax
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $('.modal').modal();

    //Materialize.showStaggeredList('.ani-loader');
});

