
$( document ).ready(function() {
    if (window.location.pathname.includes("home")) {
        $('#home').addClass('active');
    } else if (window.location.pathname.includes("dailyrecords")) {
        $('#dailyrecords').addClass('active');
    } else if (window.location.pathname.includes("approvals")) {
        $('#approvals').addClass('active');
    } else if (window.location.pathname.includes("itemregistration")) {
        $('#itemregistration').addClass('active');
    } else if (window.location.pathname.includes("stocksupplies")) {
        $('#stocksupplies').addClass('active');
    } else if (window.location.pathname.includes("balance")) {
        $('#balance').addClass('active');
    } else if (window.location.pathname.includes("chickshealth")) {
        $('#chickshealth').addClass('active');
    } else if (window.location.pathname.includes("customlogging")) {
        $('#customlogging').addClass('active');
    } else if (window.location.pathname.includes("downloads")) {
        $('#downloads').addClass('active');
    }
});