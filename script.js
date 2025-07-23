document.addEventListener('DOMContentLoaded', () => {
    const tabsContainer = document.getElementById('tabs');
    const tabContentContainer = document.getElementById('tab-content');

    const files = [
        { name: 'test_registration.py', path: 'tests/test_registration.py', lang: 'python' },
        { name: 'base_page.py', path: 'pages/base_page.py', lang: 'python' },
        { name: 'home_page.py', path: 'pages/home_page.py', lang: 'python' },
        { name: 'signup_login_page.py', path: 'pages/signup_login_page.py', lang: 'python' },
        { name: 'account_info_page.py', path: 'pages/account_info_page.py', lang: 'python' },
        { name: 'account_created_page.py', path: 'pages/account_created_page.py', lang: 'python' },
        { name: 'requirements.txt', path: 'requirements.txt', lang: 'plaintext' },
    ];

    files.forEach((file, index) => {
        const tabButton = document.createElement('button');
        tabButton.className = `whitespace-nowrap flex-shrink-0 text-sm sm:text-base font-medium border-b-2 py-2 px-3 sm:py-3 sm:px-5 focus:outline-none ${index === 0 ? 'border-indigo-500 text-indigo-600' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'}`;
        tabButton.textContent = file.name;
        tabButton.dataset.filePath = file.path;
        tabButton.dataset.lang = file.lang;
        tabsContainer.appendChild(tabButton);

        const contentDiv = document.createElement('div');
        contentDiv.id = file.path;
        contentDiv.className = index === 0 ? '' : 'hidden';
        contentDiv.innerHTML = `<pre><code class="language-${file.lang} rounded-md"></code></pre>`;
        tabContentContainer.appendChild(contentDiv);
    });

    const loadContent = async (tabButton) => {
        const filePath = tabButton.dataset.filePath;
        const lang = tabButton.dataset.lang;
        const contentDiv = document.getElementById(filePath);

        if (contentDiv.dataset.loaded) return;

        try {
            const response = await fetch(filePath);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const text = await response.text();
            const codeElement = contentDiv.querySelector('code');
            codeElement.textContent = text;
            hljs.highlightElement(codeElement);
            contentDiv.dataset.loaded = 'true';
        } catch (error) {
            contentDiv.querySelector('code').textContent = `Ошибка загрузки файла: ${filePath}\n${error}`;
        }
    };

    tabsContainer.addEventListener('click', (e) => {
        if (e.target.tagName !== 'BUTTON') return;

        const allButtons = tabsContainer.querySelectorAll('button');
        allButtons.forEach(btn => {
            btn.className = 'whitespace-nowrap flex-shrink-0 text-sm sm:text-base font-medium border-b-2 py-2 px-3 sm:py-3 sm:px-5 focus:outline-none border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300';
        });

        e.target.className = 'whitespace-nowrap flex-shrink-0 text-sm sm:text-base font-medium border-b-2 py-2 px-3 sm:py-3 sm:px-5 focus:outline-none border-indigo-500 text-indigo-600';

        const allContent = tabContentContainer.querySelectorAll('div[id]');
        allContent.forEach(content => {
            content.classList.add('hidden');
        });

        const activeContent = document.getElementById(e.target.dataset.filePath);
        activeContent.classList.remove('hidden');

        loadContent(e.target);
    });

    const firstTab = tabsContainer.querySelector('button');
    if (firstTab) {
        loadContent(firstTab);
    }
});
