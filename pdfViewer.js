pdfjsLib.GlobalWorkerOptions.workerSrc =
  'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

function initPDFViewer(containerId, pdfUrl) {
    var container = document.getElementById(containerId);
    if (!container) {
        console.error('[PDFViewer] Container not found:', containerId);
        return { load: function(){} };
    }

    var canvas    = container.querySelector('.slide-canvas');
    var ctx       = canvas.getContext('2d');
    var loader    = container.querySelector('.slide-loader');
    var dotsWrap  = container.querySelector('.slide-dots');
    var counter   = container.querySelector('.slide-counter');
    var btnPrev   = container.querySelector('.btn-prev');
    var btnNext   = container.querySelector('.btn-next');

    var pdfDoc     = null;
    var current    = 1;
    var renderTask = null;

    // ── Render ────────────────────────────────────────────────────
    function renderPage(num) {
        loader.classList.remove('hidden');
        if (renderTask) { renderTask.cancel(); renderTask = null; }

        pdfDoc.getPage(num).then(function(page) {
            // Use container width; fall back to 800 if layout not ready
            var containerWidth = container.clientWidth || 800;
            var dpr   = window.devicePixelRatio || 1;

            // Scale to fit width at device pixel ratio
            var naturalVp = page.getViewport({ scale: 1 });
            var scale     = (containerWidth / naturalVp.width) * dpr;
            var vp        = page.getViewport({ scale: scale });

            // Size canvas to actual rendered dimensions
            canvas.width  = vp.width;
            canvas.height = vp.height;

            // CSS: full width, height auto so portrait pages aren't squished
            canvas.style.width  = '100%';
            canvas.style.height = 'auto';

            renderTask = page.render({ canvasContext: ctx, viewport: vp });
            renderTask.promise.then(function() {
                renderTask = null;
                loader.classList.add('hidden');
                updateUI();
            }).catch(function() {
                renderTask = null;
            });
        }).catch(function(e) {
            console.error('[PDFViewer] getPage failed:', e);
        });
    }

    // ── UI ────────────────────────────────────────────────────────
    function updateUI() {
        var total = pdfDoc.numPages;
        counter.textContent = current + ' / ' + total;
        btnPrev.disabled = (current <= 1);
        btnNext.disabled = (current >= total);
        dotsWrap.querySelectorAll('.slide-dot').forEach(function(d, i) {
            d.classList.toggle('active', i + 1 === current);
        });
    }

    function goTo(num) {
        if (!pdfDoc) return;
        if (num < 1 || num > pdfDoc.numPages) return;
        current = num;
        renderPage(current);
    }

    btnPrev.addEventListener('click', function() { goTo(current - 1); });
    btnNext.addEventListener('click', function() { goTo(current + 1); });

    // ── Resize ────────────────────────────────────────────────────
    var resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (pdfDoc) renderPage(current);
        }, 150);
    });

    // ── Load a PDF URL into this viewer ───────────────────────────
    function loadPDF(url) {
        // Reset state
        pdfDoc  = null;
        current = 1;
        dotsWrap.innerHTML = '';
        counter.textContent = '— / —';
        btnPrev.disabled = true;
        btnNext.disabled = true;
        loader.classList.remove('hidden');

        console.log('[PDFViewer] Loading:', url);

        pdfjsLib.getDocument(url).promise.then(function(doc) {
            pdfDoc = doc;
            var total = doc.numPages;
            console.log('[PDFViewer] Loaded OK:', url, total, 'pages');

            dotsWrap.innerHTML = '';
            for (var i = 1; i <= total; i++) {
                (function(pageNum) {
                    var dot = document.createElement('button');
                    dot.className = 'slide-dot';
                    dot.title = 'Page ' + pageNum;
                    dot.addEventListener('click', function() { goTo(pageNum); });
                    dotsWrap.appendChild(dot);
                })(i);
            }

            btnPrev.disabled = false;
            btnNext.disabled = false;
            renderPage(1);

        }).catch(function(err) {
            console.error('[PDFViewer] Failed to load:', url, err);
            loader.innerHTML =
                '<p style="color:#ff9cac;font-family:monospace;font-size:.8rem;' +
                'padding:20px;text-align:center;line-height:1.8">' +
                '❌ PDF introuvable<br>' +
                '<span style="opacity:.6;font-size:.72rem">' + url + '</span></p>';
            loader.classList.remove('hidden');
        });
    }

    // Boot with initial URL
    loadPDF(pdfUrl);

    // Return control object so callers can swap PDFs
    return { load: loadPDF };
}