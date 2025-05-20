document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('summaryForm');
  const loader = document.getElementById('loader');
  const summaryPre = document.getElementById('summary');
  const modeToggle = document.getElementById('mode-toggle');
  const transcriptTextarea = document.getElementById('transcript');
  const summaryTimeEl = document.getElementById('summaryTime');
  const copyBtn = document.getElementById('copyBtn');
  const downloadTxt = document.getElementById('downloadTxt');
  const downloadPdf = document.getElementById('downloadPdf');
  const clearBtn = document.getElementById('clearbutton'); 
  const wordCountEl = document.getElementById('wordCount');
  const body = document.body;

  // dark or light mode
  modeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    modeToggle.textContent = body.classList.contains('dark-mode') ? '☀️' : '🌙';
  });

  // Clear func. for entered transcript
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      transcriptTextarea.value = '';
      transcriptTextarea.style.height = 'auto';
    });
  }

  // resize summary area
  transcriptTextarea.addEventListener('input', () => {
    transcriptTextarea.style.height = 'auto';
    transcriptTextarea.style.height = transcriptTextarea.scrollHeight + 'px';
  });

  // loader on form submit
  form.addEventListener('submit', () => {
    loader.style.display = 'block';
  });

  // Copy to clipboard 
  if (copyBtn && summaryPre) {
    copyBtn.addEventListener('click', () => {
      navigator.clipboard.writeText(summaryPre.textContent).then(() => {
        alert('Summary copied to clipboard!');
      });
    });
  }

  // Download as .txt
  if (downloadTxt && summaryPre) {
    downloadTxt.addEventListener('click', () => {
      const blob = new Blob([summaryPre.textContent], { type: 'text/plain' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'summary.txt';
      link.click();
    });
  }

  // download as PDF
  if (downloadPdf && summaryPre) {
    downloadPdf.addEventListener('click', async () => {
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF();
      const text = summaryPre.textContent;
      const lines = doc.splitTextToSize(text, 180);
      doc.text(lines, 10, 10);
      doc.save('summary.pdf');
    });
  }

  // Word count and duration
  if (summaryPre) {
    const words = summaryPre.textContent.trim().split(/\s+/).length;
    wordCountEl.textContent = `Word count: ${words}`;
    const seconds = Math.ceil(words / 2);
    summaryTimeEl.textContent = `Estimated reading time: ${seconds}s`;
  }

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
});
