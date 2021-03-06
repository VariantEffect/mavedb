"use strict";
jQuery, $;

$("document").ready(function () {
    var options = {
        // Where to render the table of contents.
        tocSelector: ".js-toc",

        // Where to grab the headings to build the table of contents.
        contentSelector: ".js-toc-content",

        // Which headings to grab inside of the contentSelector element.
        headingSelector: "h1, h2, h3, h4, h5, h6",

        // Headings that match the ignoreSelector will be skipped.
        ignoreSelector: ".js-toc-ignore",

        // Main class to add to links.
        linkClass: "toc-link",

        // Extra classes to add to links.
        extraLinkClasses: "",

        // Class to add to active links,
        // the link corresponding to the top most heading on the page.
        activeLinkClass: "is-active-link",

        // Main class to add to lists.
        listClass: "toc-list",

        // Extra classes to add to lists.
        extraListClasses: "",

        // Class that gets added when a list should be collapsed.
        isCollapsedClass: "is-collapsed",

        // Class that gets added when a list should be able
        // to be collapsed but isn"t necessarily collpased.
        collapsibleClass: "is-collapsible",

        // Class to add to list items.
        listItemClass: "toc-list-item",

        // How many heading levels should not be collpased.
        // For example, number 6 will show everything since
        // there are only 6 heading levels and number 0 will collpase them all.
        // The sections that are hidden will open
        // and close as you scroll to headings within them.
        collapseDepth: 0,

        // Smooth scrolling enabled.
        smoothScroll: true,

        // Smooth scroll duration.
        smoothScrollDuration: 420,

        // Callback for scroll end (requires: smoothScroll).
        scrollEndCallback: function (e) {},

        // Headings offset between the headings and the top of the document
        // (this is meant for minor adjustments).
        headingsOffset: 0,

        // Timeout between events firing to make sure it"s
        // not too rapid (for performance reasons).
        throttleTimeout: 50,

        // Element to add the positionFixedClass to.
        positionFixedSelector: ".js-toc",

        // Fixed position class to add to make sidebar fixed after scrolling
        // down past the fixedSidebarOffset.
        positionFixedClass: "is-position-fixed",

        // fixedSidebarOffset can be any number but by default is set
        // to auto which sets the fixedSidebarOffset to the sidebar
        // element"s offsetTop from the top of the document on init.
        fixedSidebarOffset: 250,

        // includeHtml can be set to true to include the HTML markup from the
        // heading node instead of just including the textContent.
        includeHtml: false
    };
    tocbot.init(options);
});
