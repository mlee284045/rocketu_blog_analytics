$(document).ready(function() {
    $("#featuredBlog").click(function () {
        mixpanel.track("Blog Footer Clicked");
    });

    $('.sidebarTag').click(function(e) {
        mixpanel.track("Sidebar clicked", {
            "name": e.target.data('name')
        });
    })

});