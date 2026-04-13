pdfjsLib.GlobalWorkerOptions.workerSrc =
  'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

function initPDFViewer(containerId, pdfUrl) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const canvas   = container.querySelector('.slide-canvas');
    const ctx      = canvas.getContext('2d');
    const loader   = container.querySelector('.slide-loader');
    const dotsWrap = container.querySelector('.slide-dots');
    const counter  = container.querySelector('.slide-counter');
    const btnPrev  = container.querySelector('.btn-prev');
    const btnNext  = container.querySelector('.btn-next');

    let pdfDoc     = null;
    let current    = 1;
    let renderTask = null;

    // ── Render a page ─────────────────────────────────────────────
    function renderPage(num) {
        loader.classList.remove('hidden');

        // Cancel any render already in flight
        if (renderTask) {
            renderTask.cancel();
            renderTask = null;
        }

        pdfDoc.getPage(num).then(page => {
            // clientWidth can be 0 before layout settles — fall back to 800
            const containerWidth = canvas.parentElement.clientWidth || 800;
            const dpr   = window.devicePixelRatio || 1;
            const scale = (containerWidth / page.getViewport({ scale: 1 }).width) * dpr;
            const vp    = page.getViewport({ scale });

            canvas.width  = vp.width;
            canvas.height = vp.height;

            renderTask = page.render({ canvasContext: ctx, viewport: vp });
            renderTask.promise
                .then(() => {
                    renderTask = null;
                    loader.classList.add('hidden');
                    updateUI();
                })
                .catch(() => {
                    renderTask = null;
                });
        });
    }

    // ── Sync buttons, counter and dots ────────────────────────────
    function updateUI() {
        const total = pdfDoc.numPages;
        counter.textContent = current + ' / ' + total;
        btnPrev.disabled = current <= 1;
        btnNext.disabled = current >= total;
        dotsWrap.querySelectorAll('.slide-dot').forEach(function(dot, i) {
            dot.classList.toggle('active', i + 1 === current);
        });
    }

    // ── Navigate ──────────────────────────────────────────────────
    function goTo(num) {
        if (!pdfDoc) return;
        if (num < 1 || num > pdfDoc.numPages) return;
        current = num;
        renderPage(current);
    }

    btnPrev.addEventListener('click', function() { goTo(current - 1); });
    btnNext.addEventListener('click', function() { goTo(current + 1); });

    // ── Re-render on resize ───────────────────────────────────────
    var resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (pdfDoc) renderPage(current);
        }, 150);
    });

    // ── Load PDF ──────────────────────────────────────────────────
    pdfjsLib.getDocument(pdfUrl).promise.then(function(doc) {
        pdfDoc = doc;
        var total = doc.numPages;

        // Build dot navigation
        dotsWrap.innerHTML = '';
        for (var i = 1; i <= total; i++) {
            (function(pageNum) {
                var dot = document.createElement('button');
                dot.className = 'slide-dot';
                dot.title = 'Slide ' + pageNum;
                dot.addEventListener('click', function() { goTo(pageNum); });
                dotsWrap.appendChild(dot);
            })(i);
        }

        // Enable buttons (they start disabled in the HTML)
        btnPrev.disabled = false;
        btnNext.disabled = false;

        renderPage(1);

    }).catch(function(err) {
        console.error('PDF Viewer — failed to load:', pdfUrl, err);
        loader.innerHTML =
            '<p style="color:#ff9cac;font-family:monospace;font-size:.8rem;' +
            'padding:16px;text-align:center">PDF introuvable.<br>' + pdfUrl + '</p>';
    });
}