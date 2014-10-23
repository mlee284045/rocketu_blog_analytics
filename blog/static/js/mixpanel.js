$(document).ready(function() {
    $("#featuredBlog").click(function () {
        mixpanel.track("Blog Footer Clicked");
    });

    $('.sidebarTag').click(function(e) {
        console.log(e.target.data('name'));
        mixpanel.track("Sidebar clicked", {
            "name": e.target.data('name')
        });
    })

});