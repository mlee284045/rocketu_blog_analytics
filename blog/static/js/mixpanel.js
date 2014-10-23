$(document).ready(function() {
    $("#featuredBlog").click(function () {
        mixpanel.track("Blog Footer Clicked");
    });

    $('.sidebarTag').click(function() {
        mixpanel.track("Sidebar clicked", {
            'name': 'hi'
        });
    });

});