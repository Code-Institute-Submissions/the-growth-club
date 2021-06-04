
$(document).ready(function () {
    // Sidenav Open and close
    $('.sidenav').sidenav({edge: "right"});
    // Date Picker
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});


