function createSummarizeButton(url) {
  const element = document.createElement('div');
  element.textContent = 'Summarize';
  element.className = 'summary-button';
  element.onclick = async function (e) {
    e.preventDefault();
    e.stopImmediatePropagation();
    try {
      element.textContent = 'Loading...';
      const res = await fetch('http://localhost:8080/summary', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });
      if (res.status !== 200) {
        throw new Error('Could not summarize');
      }
      const { summary } = await res.json();
      element.textContent = summary;
    } catch (err) {
      element.textContent = 'Error summarizing';
    }
  };
  return element;
}

function findAndEnrichLinks() {
  const currentHost = window.location.host;
  const links = document.querySelectorAll('a');
  for (const link of [...links]) {
    // ignore already annotated buttons
    if (link.getAttribute('data-summary') === '1') {
      continue;
    }
    const url = new URL(link.getAttribute('href'), window.location.origin);
    if (url.origin !== 'null' && url.host !== currentHost) {
      link.parentNode.append(createSummarizeButton(link.getAttribute('href')));
      // mark as annotated
      link.setAttribute('data-summary', '1');
    }
  }
}

// run on page load
findAndEnrichLinks();

// Create an observer to run on page changes
const observer = new MutationObserver(() => findAndEnrichLinks());

// Start observing the target node for configured mutations
observer.observe(document, {
  attributes: true,
  childList: true,
  subtree: true,
});
