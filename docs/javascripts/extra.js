document.addEventListener('DOMContentLoaded', function() {
    // Wait for Mermaid to finish rendering
    setTimeout(function() {
        addClickHandlersToMermaid();
    }, 1000);

    // Also add handlers when new content is loaded (for SPA navigation)
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length > 0) {
                setTimeout(addClickHandlersToMermaid, 500);
            }
        });
    });

    observer.observe(document.body, { childList: true, subtree: true });

    // Initialize search section filters
    initSearchFilters();
});

function addClickHandlersToMermaid() {
    const mermaidElements = document.querySelectorAll('.mermaid');
    
    mermaidElements.forEach(function(element) {
        // Remove existing click handlers to avoid duplicates
        element.removeEventListener('click', mermaidClickHandler);
        element.addEventListener('click', mermaidClickHandler);
        
        // Add relative positioning for the hint
        element.style.position = 'relative';
    });
}

function mermaidClickHandler(event) {
    // Prevent if already in modal
    if (event.target.closest('.diagram-modal')) {
        return;
    }
    
    openDiagramModal(this);
}

function openDiagramModal(mermaidElement) {
    // Create modal
    const modal = document.createElement('div');
    modal.className = 'diagram-modal';
    
    // Create modal content container
    const modalContent = document.createElement('div');
    modalContent.className = 'diagram-modal-content';
    
    // Clone the mermaid diagram
    const clonedDiagram = mermaidElement.cloneNode(true);
    
    // Create close button
    const closeBtn = document.createElement('div');
    closeBtn.className = 'modal-close';
    closeBtn.innerHTML = '×';
    closeBtn.title = 'Close (or click outside)';
    
    // Assemble modal
    modalContent.appendChild(closeBtn);
    modalContent.appendChild(clonedDiagram);
    modal.appendChild(modalContent);
    
    // Add to page
    document.body.appendChild(modal);
    modal.style.display = 'block';
    
    // Prevent body scrolling
    document.body.style.overflow = 'hidden';
    
    // Close handlers
    closeBtn.onclick = closeDiagramModal;
    modal.onclick = function(event) {
        if (event.target === modal) {
            closeDiagramModal();
        }
    };
    
    // Close on Escape key
    document.addEventListener('keydown', escapeHandler);
    
    function closeDiagramModal() {
        document.body.removeChild(modal);
        document.body.style.overflow = '';
        document.removeEventListener('keydown', escapeHandler);
    }
    
    function escapeHandler(event) {
        if (event.key === 'Escape') {
            closeDiagramModal();
        }
    }
}

/* ── Search section filters ─────────────────────────────────────────── */

function initSearchFilters() {
    // Content-type categories with path-based classification rules.
    // Order matters: first match wins. More specific paths go first.
    var CATEGORIES = [
        { key: 'guides',       label: 'Guides',       on: true },
        { key: 'admin',        label: 'Admin',        on: true },
        { key: 'developer',    label: 'Developer',    on: true },
        { key: 'integrations', label: 'Integrations', on: true },
        { key: 'reference',    label: 'Reference',    on: false },
        { key: 'changelog',    label: 'Changelog',    on: false }
    ];

    // Reference paths — large, dense, auto-generated or specification-heavy
    var REFERENCE_PREFIXES = [
        'admin-guide/mastermind-configuration/',
        'admin-guide/providers/site-agent/',
        'admin-guide/waldur-shell/',
        'developer-guide/core-concepts/',
        'developer-guide/plugins/',
        'developer-guide/ui/',
        'integrator-guide/APIs/'
    ];
    var REFERENCE_PATHS = [
        'developer-guide/handlers',
        'developer-guide/mixins',
        'developer-guide/offering-compliance',
        'developer-guide/support'
    ];

    // Guide paths — task-oriented, user-friendly content
    var GUIDE_PREFIXES = [
        'user-guide/',
        'admin-guide/deployment/',
        'admin-guide/debugging/',
        'admin-guide/rke2-setup/',
        'admin-guide/managing-with-ansible/',
        'developer-guide/guides/',
        'integrator-guide/ansible/',
        'integrator-guide/SDK-Examples/'
    ];

    // Track which categories are enabled (toggle state)
    var enabled = {};
    CATEGORIES.forEach(function(cat) { enabled[cat.key] = cat.on; });

    var filterBar = null;

    var searchResult = document.querySelector('[data-md-component="search-result"]');
    if (!searchResult) return;
    var resultList = searchResult.querySelector('.md-search-result__list');
    if (!resultList) return;

    // Build the filter bar
    filterBar = document.createElement('div');
    filterBar.className = 'search-filter-bar';

    CATEGORIES.forEach(function(cat) {
        filterBar.appendChild(createToggleButton(cat.key, cat.label, cat.on));
    });

    filterBar.style.display = 'none';
    searchResult.insertBefore(filterBar, resultList);

    // Observe result list for changes
    var resultsObserver = new MutationObserver(function() {
        applyFilter();
        updateCounts();
    });
    resultsObserver.observe(resultList, { childList: true });

    // Hide bar when search is cleared
    var searchInput = document.querySelector('[data-md-component="search-query"]');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            if (!searchInput.value) {
                filterBar.style.display = 'none';
            }
        });
    }

    /* ── helpers ─────────────────────────────────────────────────────── */

    function createToggleButton(key, label, isOn) {
        var btn = document.createElement('button');
        btn.className = 'search-filter-btn' + (isOn ? ' active' : '');
        btn.setAttribute('data-category', key);
        btn.textContent = label;
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            enabled[key] = !enabled[key];
            btn.classList.toggle('active', enabled[key]);
            applyFilter();
        });
        return btn;
    }

    function getPathFromItem(li) {
        var link = li.querySelector('a');
        if (!link) return '';
        var href = link.getAttribute('href') || '';
        try {
            return new URL(href, window.location.origin).pathname.replace(/^\//, '');
        } catch (e) {
            return href.replace(/^\.?\//, '');
        }
    }

    function classifyPath(path) {
        // Changelog
        if (path.indexOf('about/CHANGELOG') === 0) return 'changelog';

        // Reference — check prefixes
        for (var i = 0; i < REFERENCE_PREFIXES.length; i++) {
            if (path.indexOf(REFERENCE_PREFIXES[i]) === 0) return 'reference';
        }
        // Reference — check exact path matches
        for (var j = 0; j < REFERENCE_PATHS.length; j++) {
            if (path.indexOf(REFERENCE_PATHS[j]) === 0) return 'reference';
        }

        // Guides — check prefixes
        for (var k = 0; k < GUIDE_PREFIXES.length; k++) {
            if (path.indexOf(GUIDE_PREFIXES[k]) === 0) return 'guides';
        }

        // Fall through to section-based defaults
        var section = path.split('/')[0];
        if (section === 'admin-guide') return 'admin';
        if (section === 'developer-guide') return 'developer';
        if (section === 'integrator-guide' || section === 'integrations') return 'integrations';

        // about (non-changelog), root, etc.
        return 'guides';
    }

    function applyFilter() {
        var items = resultList.querySelectorAll(':scope > li');
        if (items.length === 0) {
            filterBar.style.display = 'none';
            return;
        }
        filterBar.style.display = '';

        for (var i = 0; i < items.length; i++) {
            var li = items[i];
            var category = classifyPath(getPathFromItem(li));
            li.style.display = enabled[category] ? '' : 'none';
        }
    }

    function updateCounts() {
        var items = resultList.querySelectorAll(':scope > li');
        var counts = {};

        for (var i = 0; i < items.length; i++) {
            var cat = classifyPath(getPathFromItem(items[i]));
            counts[cat] = (counts[cat] || 0) + 1;
        }

        var btns = filterBar.querySelectorAll('.search-filter-btn');
        for (var j = 0; j < btns.length; j++) {
            var btn = btns[j];
            var key = btn.getAttribute('data-category');
            var count = counts[key] || 0;
            var label = btn.textContent.replace(/\s*\(\d+\)$/, '');
            btn.textContent = label + ' (' + count + ')';
        }
    }
}