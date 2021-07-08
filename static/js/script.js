$(document).ready(function () {
    // Sidenav Open and close
    $(".sidenav").sidenav({edge: "left"});
    // Form select
    $("select").formSelect();
    // Tabs for profile
    $('.tabs').tabs();
    // Modal
    $('.modal').modal();
    // Date Picker
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    // Bookmark save button 
    /* Orginal code from with modifications for project:
     https://stackoverflow.com/questions/5828965/bookmark-on-click-using-jquery and https://www.tutorialrepublic.com/faq/how-to-scroll-to-the-top-of-the-page-using-jquery.php */ 
    $('.bookmark_btn').on('click', function(){
        let resource_id = $(this).attr('data-resource');
        let url = "/bookmark/" + resource_id;
        $.post(url);
        $(this).css('background-color','var(--Orange)');
    });
    // Page scroll up feature for resource page
    /* Orginal code from with modifications for project:
     https://stackoverflow.com/questions/14249998/jquery-back-to-top and https://www.tutorialrepublic.com/faq/how-to-scroll-to-the-top-of-the-page-using-jquery.php */ 
    $(window).scroll(function() {
        if ($(this).scrollTop()) {
            $('#scrollButton').fadeIn();
        } else {
            $('#scrollButton').fadeOut();
        }
    });
    
    $("#scrollButton").click(function() {
        $("html, body").animate({ 
            scrollTop: 0 
        }, "fast");
     });


    // From Task Manager walkhtrough project by Code Institute
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

// Menu items: show active page
/* Orginal code from with modifications for project:
 https://www.infoworld.com/article/3304440/setting-an-active-menu-item-based-on-the-current-url-with-jquery.html */
$(function () {
    setNavigation();
});

function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $("li a").each(function () {
        var href = $(this).attr('href');
        if (path.substring(0, href.length) === href) {
            $(this).closest('li').addClass('active');
        }
    });
}
