/* ── Mermaid readability ────────────────────────────────────────────── */

// Material renders each diagram into a closed shadow root with a stylesheet of
// its own, and three of its rules leave text unreadable in one colour scheme:
// - `.nodeLabel p` takes the theme's label colour, so a node's own `color:`
//   (from `style` or `classDef`) never reaches its text while its `fill:` does;
// - `else` labels of sequence diagrams (`.sectionTitle`) get no colour at all
//   and render black;
// - sequence numbers are white on a light circle in dark mode.
// The root is closed, so keep a handle on it when Material creates it.
var MERMAID_READABILITY_CSS =
    '.nodeLabel p { color: inherit !important; }' +
    '.sectionTitle { fill: var(--md-mermaid-sequence-loop-fg-color) !important; }' +
    '.sequenceNumber { fill: var(--waldur-mermaid-sequence-number-fg-color, var(--md-mermaid-sequence-number-fg-color)) !important; }';

(function() {
    const attachShadow = Element.prototype.attachShadow;
    Element.prototype.attachShadow = function(init) {
        const root = attachShadow.call(this, init);
        if (this.classList.contains('mermaid')) {
            new MutationObserver(function() {
                fixMermaidReadability(root);
            }).observe(root, { childList: true });
        }
        return root;
    };
})();

function fixMermaidReadability(root) {
    if (!root.querySelector('svg') || root.querySelector('style[data-readability]')) {
        return;
    }
    keepDiagramReadable(root.querySelector('svg'), root.host || root);
    const style = document.createElement('style');
    style.setAttribute('data-readability', '');
    style.textContent = MERMAID_READABILITY_CSS;
    root.appendChild(style);

    // Labels take the theme's text colour even where the theme's background is
    // not what is behind them: a node or subgraph with a fill of its own, a
    // plain node inside a filled subgraph (the theme's node fill is
    // translucent), a state-diagram note in dark mode. Where the text falls
    // below 4.5:1 against what is actually behind it, use dark or white text.
    // Labels with a colour of their own are left as they are.
    const page = parseRgba(getComputedStyle(document.body).backgroundColor) || [255, 255, 255, 1];
    const filledClusters = [];
    root.querySelectorAll('g.cluster').forEach(function(cluster) {
        const shape = cluster.querySelector('rect');
        if (shape && /fill/.test(shape.getAttribute('style') || '')) {
            const fill = parseRgba(getComputedStyle(shape).fill);
            if (fill) {
                filledClusters.push({ box: shape.getBoundingClientRect(), fill: composite(fill, page) });
            }
        }
    });
    root.querySelectorAll('g.node, g.cluster').forEach(function(group) {
        const shape = group.querySelector('rect, polygon, path, circle, ellipse');
        const fill = shape && parseRgba(getComputedStyle(shape).fill);
        if (!fill) {
            return;
        }
        let base = page;
        if (!group.classList.contains('cluster')) {
            const box = shape.getBoundingClientRect();
            const x = box.left + box.width / 2;
            const y = box.top + box.height / 2;
            const cluster = filledClusters.filter(function(c) {
                return x > c.box.left && x < c.box.right && y > c.box.top && y < c.box.bottom;
            }).pop();
            if (cluster) {
                base = cluster.fill;
            }
        }
        const background = composite(fill, base);
        group.querySelectorAll('.nodeLabel').forEach(function(label) {
            if (/color/.test(label.getAttribute('style') || '')) {
                return;
            }
            const text = parseRgba(getComputedStyle(label).color);
            if (text && contrastRatio(composite(text, background), background) >= 4.5) {
                return;
            }
            label.style.setProperty('color', relativeLuminance(background) > 0.4 ? '#1f2328' : '#ffffff', 'important');
        });
    });
}

// A wide diagram is shrunk to the column width, and a long left-to-right chain
// ends up with text a few pixels high. Keep at least this share of its natural
// size and let it scroll sideways instead.
var DIAGRAM_MIN_SCALE = 0.75;

function keepDiagramReadable(svg, container) {
    const width = svg.viewBox && svg.viewBox.baseVal ? svg.viewBox.baseVal.width : 0;
    if (!width) {
        return;
    }
    svg.style.minWidth = Math.round(width * DIAGRAM_MIN_SCALE) + 'px';
    container.style.overflowX = 'auto';
}

// [r, g, b, alpha], or null for no fill at all
function parseRgba(value) {
    const match = /rgba?\(([^)]+)\)/.exec(value || '');
    if (!match) {
        return null;
    }
    const parts = match[1].split(/[\s,/]+/).filter(Boolean).map(Number);
    const alpha = parts.length > 3 ? parts[3] : 1;
    return alpha === 0 ? null : [parts[0], parts[1], parts[2], alpha];
}

function composite(top, bottom) {
    return [0, 1, 2].map(function(i) {
        return top[i] * top[3] + bottom[i] * (1 - top[3]);
    }).concat(1);
}

function relativeLuminance(rgb) {
    const channel = rgb.map(function(value) {
        value /= 255;
        return value <= 0.03928 ? value / 12.92 : Math.pow((value + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * channel[0] + 0.7152 * channel[1] + 0.0722 * channel[2];
}

function contrastRatio(a, b) {
    const la = relativeLuminance(a.slice(0, 3));
    const lb = relativeLuminance(b.slice(0, 3));
    return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
}

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

    // D2 diagrams are inline SVG, one per colour scheme
    document.querySelectorAll('.d2 svg[data-d2-version]').forEach(function(svg) {
        keepDiagramReadable(svg, svg.parentElement);
    });

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
    // Taken before the modal adds its own .mermaid to the page
    const diagramIndex = Array.prototype.indexOf.call(document.querySelectorAll('.mermaid'), mermaidElement);

    // Create modal
    const modal = document.createElement('div');
    modal.className = 'diagram-modal';

    // Create modal content container
    const modalContent = document.createElement('div');
    modalContent.className = 'diagram-modal-content';

    // Material renders each diagram into a closed shadow root, which cloneNode
    // does not copy, and drops the source, so render it again from the page HTML
    const diagram = document.createElement('div');
    diagram.className = 'mermaid';
    renderDiagram(diagramIndex).then(function(svg) {
        diagram.innerHTML = svg;
        fixMermaidReadability(diagram);
    });

    // Create close button
    const closeBtn = document.createElement('div');
    closeBtn.className = 'modal-close';
    closeBtn.innerHTML = '×';
    closeBtn.title = 'Close (or click outside)';

    // Assemble modal
    modalContent.appendChild(closeBtn);
    modalContent.appendChild(diagram);
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

function renderDiagram(index) {
    // The cached copy is the one this page was rendered from, so the index
    // still points at the clicked diagram even after a redeploy
    return fetch(location.href, { cache: 'force-cache' })
        .then(function(response) {
            return response.text();
        })
        .then(function(html) {
            const page = new DOMParser().parseFromString(html, 'text/html');
            const source = page.querySelectorAll('.mermaid')[index].textContent;
            return mermaid.render('diagram-modal-svg', source);
        })
        .then(function(result) {
            return result.svg;
        });
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

    // Known top-level documentation sections. Used to strip any leading
    // version segment that `mike` prepends on the deployed site
    // (e.g. "latest/admin-guide/..." or "8.1.0/admin-guide/...").
    var SECTIONS = [
        'about', 'admin-guide', 'API', 'developer-guide',
        'integrations', 'integrator-guide', 'user-guide'
    ];

    function stripVersionPrefix(path) {
        // Find the earliest known section appearing as a full path segment
        // and slice the path from there, dropping any version prefix.
        var best = -1;
        for (var i = 0; i < SECTIONS.length; i++) {
            var seg = SECTIONS[i] + '/';
            var idx = path.indexOf(seg);
            while (idx !== -1) {
                if (idx === 0 || path.charAt(idx - 1) === '/') {
                    if (best === -1 || idx < best) best = idx;
                    break;
                }
                idx = path.indexOf(seg, idx + 1);
            }
        }
        return best > 0 ? path.slice(best) : path;
    }

    function classifyPath(path) {
        path = stripVersionPrefix(path);

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
        if (section === 'API') return 'reference';
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
