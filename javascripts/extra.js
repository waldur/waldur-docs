document.addEventListener('DOMContentLoaded', function() {
    // Wait for Mermaid to finish rendering
    setTimeout(function() {
        addClickHandlersToMermaid();
    }, 1000);
    
    // Also add handlers when new content is loaded (for SPA navigation)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length > 0) {
                setTimeout(addClickHandlersToMermaid, 500);
            }
        });
    });
    
    observer.observe(document.body, { childList: true, subtree: true });
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