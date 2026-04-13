function initPDFViewer(containerId, pdfUrl) {
    const container = document.getElementById(containerId);

    const canvas   = container.querySelector('.slide-canvas');
    const ctx      = canvas.getContext('2d');
    const loader   = container.querySelector('.slide-loader');
    const dotsWrap = container.querySelector('.slide-dots');
    const counter  = container.querySelector('.slide-counter');
    const btnPrev  = container.querySelector('.btn-prev');
    const btnNext  = container.querySelector('.btn-next');

    let pdfDoc = null;
    let current = 1;

    function renderPage(num) {
        loader.classList.remove('hidden');

        pdfDoc.getPage(num).then(page => {
            const viewport = page.getViewport({ scale: 1 });

            canvas.width = viewport.width;
            canvas.height = viewport.height;

            page.render({
                canvasContext: ctx,
                viewport: viewport
            }).promise.then(() => {
                loader.classList.add('hidden');
                updateUI();
            });
        });
    }

    function updateUI() {
        const total = pdfDoc.numPages;
        counter.textContent = `${current} / ${total}`;
        btnPrev.disabled = current <= 1;
        btnNext.disabled = current >= total;
    }

    btnPrev.addEventListener('click', () => {
        current--;
        renderPage(current);
    });

    btnNext.addEventListener('click', () => {
        current++;
        renderPage(current);
    });

    pdfjsLib.getDocument(pdfUrl).promise.then(doc => {
        pdfDoc = doc;
        renderPage(1);
    });
}