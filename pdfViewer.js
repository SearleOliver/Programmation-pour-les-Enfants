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
    let rendering  = false;
    let renderTask = null;

    // ── Render a given page number ────────────────────────────────
    function renderPage(num) {
        if (rendering) return;
        rendering = true;
        loader.classList.remove('hidden');

        pdfDoc.getPage(num).then(page => {
            const wrap  = canvas.parentElement;
            const dpr   = window.devicePixelRatio || 1;
            const scale = (wrap.clientWidth / page.getViewport({ scale: 1 }).width) * dpr;
            const vp    = page.getViewport({ scale });

            canvas.width  = vp.width;
            canvas.height = vp.height;

            if (renderTask) renderTask.cancel();
            renderTask = page.render({ canvasContext: ctx, viewport: vp });

            renderTask.promise.then(() => {
                rendering  = false;
                renderTask = null;
                loader.classList.add('hidden');
                updateUI();
            }).catch(() => {
                rendering = false;
            });
        });
    }

    // ── Update buttons, counter and dots ─────────────────────────
    function updateUI() {
        const total = pdfDoc.numPages;
        counter.textContent = `${current} / ${total}`;

        // Enable / disable nav buttons
        btnPrev.disabled = current <= 1;
        btnNext.disabled = current >= total;

        // Highlight correct dot
        dotsWrap.querySelectorAll('.slide-dot').forEach((dot, i) => {
            dot.classList.toggle('active', i + 1 === current);
        });
    }

    // ── Navigate to a page ────────────────────────────────────────
    function goTo(num) {
        if (!pdfDoc) return;
        if (num < 1 || num > pdfDoc.numPages) return;
        if (num === current) return;
        current = num;
        renderPage(current);
    }

    // ── Button clicks ─────────────────────────────────────────────
    btnPrev.addEventListener('click', () => goTo(current - 1));
    btnNext.addEventListener('click', () => goTo(current + 1));

    // ── Keyboard arrows (only when this viewer is in the viewport) ─
    //document.addEventListener('keydown', e => {
    //    const rect = container.getBoundingClientRect();
    //    const visible = rect.top < window.innerHeight && rect.bottom > 0;
    //    if (!visible) return;
    //    if (['ArrowRight', 'ArrowDown'].includes(e.key)) goTo(current + 1);
    //    if (['ArrowLeft',  'ArrowUp'  ].includes(e.key)) goTo(current - 1);
    //});

    // ── Re-render on window resize (debounced) ───────────────────
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            if (pdfDoc) renderPage(current);
        }, 150);
    });

    // ── Load PDF ──────────────────────────────────────────────────
    pdfjsLib.getDocument(pdfUrl).promise.then(doc => {
        pdfDoc = doc;
        const total = doc.numPages;

        // Build one dot per page
        dotsWrap.innerHTML = '';
        for (let i = 1; i <= total; i++) {
            const dot = document.createElement('button');
            dot.className = 'slide-dot';
            dot.title = `Slide ${i}`;
            dot.addEventListener('click', () => goTo(i));
            dotsWrap.appendChild(dot);
        }

        // Enable buttons and render first page
        btnPrev.disabled = false;
        btnNext.disabled = false;
        renderPage(1);

    }).catch(err => {
        console.error('PDF Viewer — failed to load:', pdfUrl, err);
        loader.innerHTML =
            '<p style="color:#ff9cac;font-family:monospace;font-size:.8rem;padding:16px;text-align:center">' +
            'PDF introuvable.<br>' + pdfUrl + '</p>';
    });
}