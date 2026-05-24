pdfjsLib.GlobalWorkerOptions.workerSrc =
  'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

/* ══════════════════════════════════════════════════════════════
   initPDFViewer  —  paginated slide viewer (one page at a time)
   Used for: presentation slides
   ══════════════════════════════════════════════════════════════ */
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

    function renderPage(num) {
        loader.classList.remove('hidden');
        if (renderTask) { renderTask.cancel(); renderTask = null; }

        pdfDoc.getPage(num).then(function(page) {
            var containerWidth = container.clientWidth || 800;
            var dpr   = window.devicePixelRatio || 1;
            var naturalVp = page.getViewport({ scale: 1 });
            var scale = (containerWidth / naturalVp.width) * dpr;
            var vp    = page.getViewport({ scale: scale });

            canvas.width  = vp.width;
            canvas.height = vp.height;
            canvas.style.width  = '100%';
            canvas.style.height = 'auto';

            renderTask = page.render({ canvasContext: ctx, viewport: vp });
            renderTask.promise.then(function() {
                renderTask = null;
                loader.classList.add('hidden');
                updateUI();
            }).catch(function() { renderTask = null; });
        }).catch(function(e) {
            console.error('[PDFViewer] getPage failed:', e);
        });
    }

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

    var resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (pdfDoc) renderPage(current);
        }, 150);
    });

    function loadPDF(url) {
        pdfDoc  = null;
        current = 1;
        dotsWrap.innerHTML  = '';
        counter.textContent = '— / —';
        btnPrev.disabled    = true;
        btnNext.disabled    = true;
        loader.classList.remove('hidden');

        pdfjsLib.getDocument(url).promise.then(function(doc) {
            pdfDoc = doc;
            var total = doc.numPages;

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

    loadPDF(pdfUrl);
    return { load: loadPDF };
}


/* ══════════════════════════════════════════════════════════════
   initScrollViewer  —  all pages stacked, scrollable
   Used for: A4 portrait TP documents
   ══════════════════════════════════════════════════════════════ */
function initScrollViewer(containerId, pdfUrl) {
    var container = document.getElementById(containerId);
    if (!container) {
        console.error('[ScrollViewer] Container not found:', containerId);
        return { load: function(){} };
    }

    var pagesWrap = container.querySelector('.scroll-pages');
    var loader    = container.querySelector('.scroll-loader');
    var counter   = container.querySelector('.scroll-counter');

    function loadPDF(url) {
        // Clear previous content
        pagesWrap.innerHTML  = '';
        counter.textContent  = '';
        loader.classList.remove('hidden');

        pdfjsLib.getDocument(url).promise.then(function(doc) {
            var total = doc.numPages;
            counter.textContent = total + ' page' + (total > 1 ? 's' : '');

            // Render pages one by one, appending each canvas
            var rendered = 0;

            function renderNext(pageNum) {
                doc.getPage(pageNum).then(function(page) {
                    var containerWidth = pagesWrap.clientWidth || container.clientWidth || 800;
                    var dpr   = window.devicePixelRatio || 1;
                    var naturalVp = page.getViewport({ scale: 1 });
                    var scale = (containerWidth / naturalVp.width) * dpr;
                    var vp    = page.getViewport({ scale: scale });

                    var pageWrap = document.createElement('div');
                    pageWrap.className = 'scroll-page';

                    // Page number badge
                    var badge = document.createElement('div');
                    badge.className = 'scroll-page-num';
                    badge.textContent = pageNum + ' / ' + total;
                    pageWrap.appendChild(badge);

                    var cv = document.createElement('canvas');
                    cv.width  = vp.width;
                    cv.height = vp.height;
                    cv.style.width  = '100%';
                    cv.style.height = 'auto';
                    cv.style.display = 'block';
                    pageWrap.appendChild(cv);

                    pagesWrap.appendChild(pageWrap);

                    page.render({ canvasContext: cv.getContext('2d'), viewport: vp }).promise.then(function() {
                        rendered++;
                        if (rendered === 1) {
                            // Hide loader once first page is visible
                            loader.classList.add('hidden');
                        }
                        if (pageNum < total) {
                            renderNext(pageNum + 1);
                        }
                    });
                });
            }

            renderNext(1);

        }).catch(function(err) {
            console.error('[ScrollViewer] Failed to load:', url, err);
            loader.innerHTML =
                '<p style="color:#ff9cac;font-family:monospace;font-size:.8rem;' +
                'padding:20px;text-align:center;line-height:1.8">' +
                '❌ PDF introuvable<br>' +
                '<span style="opacity:.6;font-size:.72rem">' + url + '</span></p>';
        });
    }

    loadPDF(pdfUrl);
    return { load: loadPDF };
}