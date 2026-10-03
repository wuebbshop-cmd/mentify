(function () {
    function clamp(value, minimum, maximum) {
        return Math.max(minimum, Math.min(maximum, value));
    }

    function initializeEditor(editor) {
        const stage = editor.querySelector(".visual-crop-stage");
        const image = editor.querySelector(".visual-source-page");
        const selection = editor.querySelector(".visual-crop-selection");
        const bboxField = document.getElementById("id_bbox");
        const pageWidth = Number(editor.dataset.pageWidth);
        const pageHeight = Number(editor.dataset.pageHeight);
        const minimumSize = 20;
        if (!stage || !image || !selection || !bboxField || !pageWidth || !pageHeight) {
            return;
        }

        let savedBbox;
        let currentBbox;
        try {
            savedBbox = JSON.parse(editor.dataset.savedBbox);
            currentBbox = JSON.parse(bboxField.value || editor.dataset.savedBbox);
        } catch (_) {
            return;
        }

        function constrain(box) {
            let x0 = Number(box[0]);
            let y0 = Number(box[1]);
            let x1 = Number(box[2]);
            let y1 = Number(box[3]);
            if (x0 > x1) [x0, x1] = [x1, x0];
            if (y0 > y1) [y0, y1] = [y1, y0];
            x0 = clamp(x0, 0, pageWidth - minimumSize);
            y0 = clamp(y0, 0, pageHeight - minimumSize);
            x1 = clamp(x1, x0 + minimumSize, pageWidth);
            y1 = clamp(y1, y0 + minimumSize, pageHeight);
            return [x0, y0, x1, y1];
        }

        function render() {
            if (!image.clientWidth || !image.clientHeight) return;
            currentBbox = constrain(currentBbox);
            selection.style.left = `${(currentBbox[0] / pageWidth) * 100}%`;
            selection.style.top = `${(currentBbox[1] / pageHeight) * 100}%`;
            selection.style.width = `${((currentBbox[2] - currentBbox[0]) / pageWidth) * 100}%`;
            selection.style.height = `${((currentBbox[3] - currentBbox[1]) / pageHeight) * 100}%`;
            bboxField.value = JSON.stringify(currentBbox.map((value) => Math.round(value * 100) / 100));
        }

        function pagePoint(event) {
            const bounds = stage.getBoundingClientRect();
            return {
                x: clamp(((event.clientX - bounds.left) / bounds.width) * pageWidth, 0, pageWidth),
                y: clamp(((event.clientY - bounds.top) / bounds.height) * pageHeight, 0, pageHeight),
            };
        }

        let drag = null;
        stage.addEventListener("pointerdown", (event) => {
            if (event.button !== 0) return;
            const handle = event.target.closest(".visual-crop-handle");
            const point = pagePoint(event);
            drag = {
                mode: handle ? handle.dataset.edge : selection.contains(event.target) ? "move" : "new",
                start: point,
                bbox: currentBbox.slice(),
            };
            stage.setPointerCapture(event.pointerId);
            event.preventDefault();
        });

        stage.addEventListener("pointermove", (event) => {
            if (!drag) return;
            const point = pagePoint(event);
            const dx = point.x - drag.start.x;
            const dy = point.y - drag.start.y;
            const next = drag.bbox.slice();
            if (drag.mode === "new") {
                currentBbox = [drag.start.x, drag.start.y, point.x, point.y];
            } else if (drag.mode === "move") {
                const width = next[2] - next[0];
                const height = next[3] - next[1];
                next[0] = clamp(next[0] + dx, 0, pageWidth - width);
                next[1] = clamp(next[1] + dy, 0, pageHeight - height);
                next[2] = next[0] + width;
                next[3] = next[1] + height;
                currentBbox = next;
            } else {
                if (drag.mode.includes("w")) next[0] = drag.bbox[0] + dx;
                if (drag.mode.includes("e")) next[2] = drag.bbox[2] + dx;
                if (drag.mode.includes("n")) next[1] = drag.bbox[1] + dy;
                if (drag.mode.includes("s")) next[3] = drag.bbox[3] + dy;
                currentBbox = next;
            }
            render();
        });

        function finishDrag() {
            if (drag) {
                currentBbox = constrain(currentBbox);
                render();
                drag = null;
            }
        }

        stage.addEventListener("pointerup", finishDrag);
        stage.addEventListener("pointercancel", finishDrag);
        image.addEventListener("load", render);
        if (image.complete) render();

        editor.querySelector(".visual-crop-reset")?.addEventListener("click", () => {
            currentBbox = savedBbox.slice();
            render();
        });
        window.addEventListener("resize", render);
    }

    document.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll(".visual-crop-editor").forEach(initializeEditor);
    });
})();